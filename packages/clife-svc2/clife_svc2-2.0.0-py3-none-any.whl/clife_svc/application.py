import os
if os.environ.get("ENVIRONMENT"):
    from gevent import monkey
    monkey.patch_all()

import re
import time
import threading
from typing import Any, Callable, List, Optional, Set, Union

from flask import Flask, request
from flask_cors import CORS

from clife_svc.libs import utils
from clife_svc.libs.context import app_id, request_id
from clife_svc.config.disconf import Disconf
from clife_svc.config.configmap import ConfigMap
from clife_svc.errors.error_code import ApiException
from clife_svc.libs.http_request import ClientRequest
from clife_svc.libs.log import init_log, klogger, plogger
from clife_svc.libs.mq_handler import MQHandler


def before_request():
    """在处理请求前打印请求信息"""
    # 生成请求标识
    app_id.set(request.args.get('appId'))
    request_id.set(utils.tid_maker())

    request.start_time = time.time()
    logger = plogger if request.path == '/time' else klogger
    logger.info('Request URL: {} {}'.format(request.method, request.url))
    if request.args:
        logger.info('Request Params: {}'.format(request.args.to_dict()))
    if request.method == 'POST' and request.is_json:
        logger.info('Request Body: {}'.format(request.json))


def after_request(response):
    """在处理请求后打印返回信息"""
    logger = plogger if request.path == '/time' else klogger
    logger.info('Request Cost: {}s'.format(round(time.time() - request.start_time, 2)))  # noqa
    if response.json:
        logger.info('Response Content: {}'.format(response.json))
    logger.info('Response HTTP Status Code: {}'.format(response.status_code))
    return response


def probe():
    """k8s 探针 http监控服务请求地址"""
    result = {'code': 0,
              'msg': 'success',
              'data': {
                  'time': time.strftime('%Y-%m-%d-%H-%M', time.localtime())
              }}
    if 'q' in request.args:
        result['data']['q'] = request.args['q']
    return result


def api_exception_handler(error):
    """拦截接口抛出的所有自定义的HTTPException 异常"""
    klogger.exception('Request Exception:'.format())
    response = {
        "code": error.error_code,
        "msg": error.description,
        "data": error.response
    }
    return response, error.code


def app_exception(error):
    """拦截接口抛出的所有未知非HTTPException 异常"""
    klogger.exception('Request Exception:'.format())
    response = {
        "code": 10024,
        "msg": 'Unknown error',
    }
    return response, 500


class App:
    """
    http接口服务上下文对象，单实例对象
    """
    _instance = None
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        """
        实现单例模式
        """
        if not cls._instance:
            with cls._instance_lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, app_name, log_root_path='/www/logs', conf='', log_level='DEBUG'):
        """
        构造函数
        :param app_name 项目名称
        :param log_root_path 项目输出的日志根路径，推荐使用/www/logs，便于线上统一采集日志
        :param conf: 配置文件名称列表，提供字符串列表或逗号分隔字符串
        :param log_level: 日志收集器级别，从低到高依次为 TRACE|DEBUG|INFO|SUCCESS|WARNING|ERROR|CRITICAL
        """
        self.app_name = app_name
        if not re.match(r'^([a-zA-Z0-9]+-?[a-zA-Z0-9]+)+$', app_name):
            raise Exception('app_name can only be letters, numbers, or strike-through!')

        init_log(os.path.join(log_root_path, app_name), log_level=log_level)

        self.__disConf = Disconf('clife-ai', '0.0.1-SNAPSHOT', conf).get_disconf()
        self.__configMap = ConfigMap()

        self.__client = ClientRequest(self)
        self.__mqHandler = MQHandler(self)

        self.__flask = Flask(app_name)
        self.__flask.json.ensure_ascii = False  # 解决中文乱码问题

    def init_api(self) -> Flask:
        """
        在App中初始化服务接口
        :return: FastAPI，作为服务器运行入口对象
        """
        CORS(self.__flask)
        self.__flask.before_request(before_request)
        self.__flask.after_request(after_request)
        self.__flask.register_error_handler(ApiException, api_exception_handler)
        self.__flask.register_error_handler(Exception, app_exception)
        self.__flask.add_url_rule('/time', endpoint='time', view_func=probe)
        self.__mqHandler.start_consumer()
        return self.__flask

    def get_conf(self, key: str, default: str = '') -> str:
        """
        获取配置项,优先级按照disconf, configmap, 环境变量顺序获取
        """
        if key in self.__disConf:
            return self.__disConf.get(key)
        item = self.__configMap.get(key)
        if item:
            return item
        item = utils.get_env(key)
        if item:
            return item
        return default

    def get_conf_list(self, key: str, default: list = None) -> list:
        """
        获取列表形式配置数据
        :param key:配置项的key
        :param default:配置项默认值
        :return:
        """
        if default is None:
            default = []
        values = self.get_conf(key)
        if values:
            return values.split(',')
        return default

    def get_all_conf(self) -> dict:
        """
        获取所有配置数据
        :return:
        """
        all_config = {}
        all_config.update(self.__disConf)
        all_config.update(self.__configMap.get_all())
        return all_config

    def add_api(self, path: str, view_func: Callable[..., Any], methods: Optional[Union[Set[str], List[str]]] = None):
        """
        增加服务接口，此函数需要在init_api前调用
        :param path:接口访问路径
        :param view_func:接口实现函数
        :param methods:接口访问方式，如GET、POST等
        :return:
        """
        self.__flask.add_url_rule(path, view_func=view_func, methods=methods)

    def add_subscribe(self, call_back, topic=None):
        """
        :param call_back:回调函数
        :param topic:订阅主题
        """
        self.__mqHandler.add_subscribe(call_back, topic)

    def download_file(self, file_url, retry=2, timeout=None):
        """
        下载文件
        :param file_url:文件地址
        :param retry:失败重试次数，默认为2次，建议不大于3次
        :param timeout: 文件下载超时时间（秒），默认为配置文件ai-commons.properties中http.timeout，目前为15秒
        :return:文件数据字节数组
        """
        return self.__client.download_file(file_url, retry, timeout)

    def download_models(self, file_names, retry=2):
        """
        下载文件
        :param file_names:模型文件名列表
        :param retry:失败重试次数，默认为2次，建议不大于3次
        :return: 模型目录路径
        """
        local_model_dir = "/mnt/models"
        os.makedirs(local_model_dir, exist_ok=True)
        for file_name in file_names:
            file_path = local_model_dir + '/' + file_name
            if os.path.exists(file_path):
                continue
            self.__client.download_s3_file(file_name, file_path, retry)
        return local_model_dir

    def upload_file(self, file_path: str, retry=2) -> str:
        """
        :param file_path:本地文件路径
        :param retry:失败重试次数，默认为2次，建议不大于3次
        :return: 文件url
        """
        return self.__client.upload_file(file_path, retry)

    def upload_file_from_buffer(self, file_extension: str, body, retry=2) -> str:
        """
        :param file_extension: 文件扩展名，如.txt|.png
        :param body: 文件流,必须实现了read方法
        :param retry: 失败重试次数,默认为2次，建议不大于3次
        :return: 文件url
        """
        return self.__client.upload_file_from_buffer(file_extension, body, retry)

    def send_mq_msg(self, body, topic=None, keys=None, tags=None):
        """
        :param body: rocketMQ消息内容
        :param topic: rocketMQ消息主题，非必传，未配置默认主题时必传
        :param keys: rocketMQ消息唯一标识，非必传
        :param tags: rocketMQ消息标签，非必传
        """
        self.__mqHandler.send_sync(body, topic, keys, tags)

    def call_back(self, url: str, body: dict, retry=2, timeout=None):
        """
        推理结果回调
        :param url:回调地址
        :param body:回调内容，字典中必须包含‘uuid’的key，且value符合UUID规则
        :param retry:失败重试次数，默认为2次，建议不大于3次
        :param timeout: 回调超时时间（秒），默认为配置文件ai-commons.properties中http.timeout，目前为15秒
        :return:回调请求响应体
        """
        if not re.match(r'[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}', body.get('uuid', '')):
            raise Exception('The request body of call back must contain the correct UUID.')
        return self.__client.call_back(url, body, retry, timeout)

