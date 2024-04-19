import os
import time
import random
import string

import boto3
import mimetypes
import requests
import qcloud_cos

from clife_svc.libs.log import klogger, clogger
from clife_svc.errors.error_code import ParameterException, UploadFileException, TimeoutException, \
    DownloadFileException, CallBackException


class ClientRequest:

    def __init__(self, app):
        self.HTTP_TIMEOUT = int(app.get_conf('http.timeout', 5))

        self.S3_TYPE = None
        self.S3_KEY = app.app_name
        self.MODEL_KEY = f"model-repository/{self.S3_KEY}/"

        self.S3_ENDPOINT_URL = app.get_conf('s3.endpoint.url', '')
        self.S3_ACCESS_KEY = app.get_conf('s3.access.key', '')
        self.S3_SECRET_KEY = app.get_conf('s3.secret.key', '')
        self.S3_BUCKET = app.get_conf('s3.bucket', '')
        self.S3_BUCKET_PRIVATE = int(app.get_conf('s3.bucket.private', '0'))

        self.COS_REGION = app.get_conf('cos.region', '')
        self.COS_SECRET_ID = app.get_conf('cos.secret.id', '')
        self.COS_SECRET_KEY = app.get_conf('cos.secret.key', '')
        self.COS_BUCKET = app.get_conf('cos.bucket', '')
        self.COS_BUCKET_HOST = app.get_conf('cos.bucket.host', 'cos.clife.net')

        if all((self.S3_ENDPOINT_URL, self.S3_ACCESS_KEY, self.S3_SECRET_KEY, self.S3_BUCKET)):
            self.S3_TYPE = 'S3'
            clogger.info('S3 Client parameters check success')
        elif all((self.COS_REGION, self.COS_SECRET_ID, self.COS_SECRET_KEY, self.COS_BUCKET)):
            self.S3_TYPE = 'COS'
            clogger.info('COS Client parameters check success')
        else:
            clogger.warning('Both S3 and COS Client missing required parameters, Object Storage disabled.')

        if self.S3_TYPE:
            clogger.info(f'Object Storage System: {self.S3_TYPE}')
            clogger.info(f'Object Storage Model Key: {self.S3_BUCKET}/{self.MODEL_KEY}')
            try:
                if self.S3_TYPE == 'COS':
                    self.COS_CONFIG = qcloud_cos.CosConfig(Region=self.COS_REGION,
                                                           Secret_id=self.COS_SECRET_ID,
                                                           Secret_key=self.COS_SECRET_KEY)
                    self.S3_CLIENT = qcloud_cos.CosS3Client(self.COS_CONFIG)
                else:
                    self.S3_CLIENT = boto3.client(service_name='s3',
                                                  aws_access_key_id=self.S3_ACCESS_KEY,
                                                  aws_secret_access_key=self.S3_SECRET_KEY,
                                                  endpoint_url=self.S3_ENDPOINT_URL,)
            except Exception:  # noqa
                clogger.warning('Create Object Storage Client fails, Object Storage disabled.')

    def download_s3_file(self, file_name: str, local_file_path: str, retry=2):
        """
        腾讯云cos或S3下载文件至本地
        :param file_name 待下载的文件名
        :param local_file_path 下载的目标路径
        :param retry 失败重试次数
        """
        if not self.S3_TYPE:
            raise DownloadFileException('Object Storage disabled.')
        key = self.MODEL_KEY + file_name

        while True:
            klogger.info(f'Start download s3 file: {file_name}')
            start = time.time()

            try:
                if self.S3_TYPE == 'COS':
                    self.S3_CLIENT.download_file(Bucket=self.COS_BUCKET, Key=key, DestFilePath=local_file_path)
                else:
                    self.S3_CLIENT.download_file(Bucket=self.S3_BUCKET, Key=key, Filename=local_file_path)  # noqa
                klogger.info('Success download s3 file, download cost: {}s'.format(round(time.time() - start, 2)))
                return
            except Exception as e:
                if retry != 0:
                    klogger.warning('Error download file, retry left: {}'.format(retry))
                    retry -= 1
                    continue
                raise Exception(f'Download file failed, file name: {file_name}')

    def download_file(self, file_url, retry=2, timeout=None):
        """
        图片下载，仅支持公有读权限的文件资源下载
        :param file_url:
        :param retry:
        :param timeout:
        :return: 文件字节数组
        """
        if file_url.startswith('http'):
            timeout = timeout or self.HTTP_TIMEOUT
            # 获取或者创建对应的会话对象
            while True:
                klogger.info('Start download file: {}'.format(file_url))
                start = time.time()
                try:
                    resp = requests.get(file_url, timeout=timeout or self.HTTP_TIMEOUT)
                    if not resp.ok:
                        raise DownloadFileException(data='Download file failed, url:{}'.format(file_url))
                    klogger.info('Download file cost: {}s'.format(round(time.time() - start, 2)))
                    klogger.info('Success download file.')
                    return resp.content
                except Exception as e:
                    if retry != 0:
                        klogger.warning('Error download file,retry left: {}'.format(retry))
                        retry -= 1
                        # 阶梯式增加每次重试的超时时间50%
                        timeout = int(timeout * 1.5)
                        continue
                    # 超时类型异常
                    if isinstance(e, requests.exceptions.Timeout):
                        raise TimeoutException(data='Download file timeout, url:{}'.format(file_url))
                    raise DownloadFileException(data='Download file failed, url:{}'.format(file_url))
        else:
            # 本地文件路径格式直接返回
            klogger.info('Local file path: {}'.format(file_url))
            return ''

    @staticmethod
    def rename_file(extension: str):
        """文件更名"""
        salt = f'{"".join(random.sample(string.ascii_letters + string.digits, 8))}{int(time.time())}'
        return salt + extension

    def upload_file(self, file_path: str, retry=2) -> str:
        """
        上传文件至腾讯云cos
        :param file_path 待上传的本地文件路径
        :param retry 失败重试次数
        :return 文件url
        """
        if not self.S3_TYPE:
            raise UploadFileException('Object Storage disabled.')

        if not os.path.isfile(file_path):
            raise ParameterException(data='File not exist:'.format(file_path))

        file_name = self.rename_file(os.path.splitext(file_path)[1])
        key = self.S3_KEY + '/' + file_name

        while retry > 0:
            retry -= 1
            start = time.time()

            try:
                if self.S3_TYPE == 'COS':
                    self.S3_CLIENT.upload_file(Bucket=self.COS_BUCKET, LocalFilePath=file_path, Key=key)
                    file_url = self.COS_CONFIG.uri(bucket=self.COS_BUCKET, path=key, domain=self.COS_BUCKET_HOST)
                else:
                    self.S3_CLIENT.upload_file(Filename=file_path, Bucket=self.S3_BUCKET, Key=key)  # noqa
                    file_url = self.S3_CLIENT.generate_presigned_url('get_object',
                                                                     Params={'Bucket': self.S3_BUCKET, 'Key': key},
                                                                     ExpiresIn=600)
                    file_url = file_url if self.S3_BUCKET_PRIVATE else file_url.split('?')[0]
                klogger.info('Upload file cost: {}s'.format(round(time.time() - start, 2)))
                klogger.info('Upload file success: {}'.format(file_url))
                return file_url
            except Exception as e:  # noqa
                klogger.warning('Error upload file,retry left: {}'.format(retry + 1))
                continue
        raise UploadFileException

    def upload_file_from_buffer(self, file_extension: str, body, retry=2) -> str:
        """
        :param file_extension: 文件扩展名，如.txt|.png
        :param body: 文件流,必须实现了read方法
        :param retry: 失败重试次数
        :return: 文件url
        """
        if not self.S3_TYPE:
            raise UploadFileException('Object Storage disabled.')

        file_name = self.rename_file(file_extension)
        key = self.S3_KEY + '/' + file_name

        while retry >= 0:
            retry -= 1
            start = time.time()

            try:
                if self.S3_TYPE == 'COS':
                    self.S3_CLIENT.upload_file_from_buffer(Bucket=self.COS_BUCKET, Key=key, Body=body)
                    file_url = self.COS_CONFIG.uri(bucket=self.COS_BUCKET, path=key, domain=self.COS_BUCKET_HOST)
                else:
                    content_type, encoding = mimetypes.guess_type(key)
                    content_type = content_type or 'application/octet-stream'
                    self.S3_CLIENT.upload_fileobj(Fileobj=body, Bucket=self.S3_BUCKET, Key=key,
                                                  ExtraArgs={"ContentType": content_type})  # noqa
                    file_url = self.S3_CLIENT.generate_presigned_url('get_object',
                                                                     Params={'Bucket': self.S3_BUCKET, 'Key': key},
                                                                     ExpiresIn=600)
                    file_url = file_url if self.S3_BUCKET_PRIVATE else file_url.split('?')[0]
                klogger.info('Upload file cost: {}s'.format(round(time.time() - start, 2)))
                klogger.info('Upload file success: {}'.format(file_url))
                return file_url
            except:  # noqa
                klogger.warning('Error upload file,retry left: {}'.format(retry + 1))
                continue
        raise UploadFileException

    def call_back(self, url: str, body: dict, retry=2, timeout=None):
        while retry > 0:
            retry -= 1
            klogger.info('Start call back: UUID:{}, URL:{}, Body: {}'.format(body.get('uuid'), url, body))
            start = time.time()
            try:
                resp = requests.post(url, json=body, timeout=timeout or self.HTTP_TIMEOUT)
                if not resp.ok:
                    raise Exception
                klogger.info('Call back cost: {}s'.format(round(time.time() - start, 2)))
                klogger.info('Success call back.')
                return resp.json()
            except Exception as e:
                if retry > 0:
                    klogger.warning('Error call back,retry left: {}'.format(retry + 1))
                    continue
                if isinstance(e, requests.exceptions.Timeout):
                    raise TimeoutException(data='Call back timeout')
                raise CallBackException(data='Call back timeout')
