import os
import sys

from loguru import logger as klogger
from flask import g

from clife_svc.libs.context import app_id, request_id


def _console_log_filter(record) -> bool:
    record['app_id'] = app_id.get()
    record['request_id'] = request_id.get()
    return True


def _format(record):
    if 'request_id' in record and record['request_id']:
        if 'app_id' in record and record['app_id']:
            return "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | " \
                   "<level>{level: <8}</level> | " \
                   "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | " \
                   "<magenta>{request_id}</magenta> | " \
                   "<blue>{app_id}</blue> | " \
                   "<level>{message}</level>\n{exception}"
        return "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | " \
               "<level>{level: <8}</level> | " \
               "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | " \
               "<magenta>{request_id}</magenta> | " \
               "<level>{message}</level>\n{exception}"
    else:
        return "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | " \
               "<level>{level: <8}</level> | " \
               "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | " \
               "<level>{message}</level>\n{exception}"


klogger.remove(handler_id=None)
std_handler_id = klogger.add(sink=sys.stderr, format=_format)
plogger = klogger.bind(probe=True)
clogger = klogger.bind(config=True)


def init_log(log_path: str, log_level='INFO'):
    """
    初始化服务日志模块
    :param log_path: 日志输出路径
    :param log_level: 日志级别，从低到高依次为 TRACE|DEBUG|INFO|SUCCESS|WARNING|ERROR|CRITICAL
    :return:
    """
    klogger.remove(handler_id=std_handler_id)

    # 控制台日志
    klogger.add(sink=sys.stderr, level=log_level, filter=_console_log_filter, format=_format)

    # 配置项日志
    klogger.add(sink=os.path.join(log_path, 'config.log'), format=_format,
                filter=lambda record: record['extra'].get('config'))

    # 探针日志
    klogger.add(sink=os.path.join(log_path, 'probe.log'), format=_format, retention='1 week',
                filter=lambda record: record['extra'].get('probe'))
    # 通用日志
    klogger.add(sink=os.path.join(log_path, '{time:YYYY-MM-DD}.log'),
                format=_format,
                level=log_level,
                enqueue=True,
                rotation='00:00',
                retention='10 days',
                encoding='utf-8',
                compression='zip',
                filter=lambda record: not record['extra'].get('time') and not record['extra'].get('config'))
