from werkzeug.exceptions import HTTPException


class ApiException(HTTPException):
    status_code: int = 500  # 响应状态码
    error_code: int = 10000  # 错误状态码
    msg: str = 'Server error'

    def __init__(
        self,
        data=None,
    ) -> None:
        self.code = self.status_code
        self.description = self.msg
        self.response = data or {}


class ParameterException(ApiException):
    """
    参数异常
    error_code
    """
    status_code = 400
    error_code = 10001
    msg = 'Invalid parameter'


class TimeoutException(ApiException):
    """
    超时异常
    """
    status_code = 500
    error_code = 10002
    msg = 'Request timeout'


class DownloadFileException(ApiException):
    """
    文件下载异常
    error_code
    """
    status_code = 400
    error_code = 10003
    msg = 'File download failed'


class UploadFileException(ApiException):
    """
    文件上传异常
    """
    status_code = 400
    error_code = 10004
    msg = 'File upload failed'


class SoException(ApiException):
    """
    so库错误
    """
    status_code = 500
    error_code = 10005
    msg = 'So error'


class ContentException(ApiException):
    """
    内容错误
    """
    status_code = 400
    error_code = 10006
    msg = 'Content error'


class DecodeImageException(ApiException):
    """
    图片解码错误
    """
    status_code = 400
    error_code = 10007
    msg = 'Decode image error'


class EncodeImageException(ApiException):
    """
    图片编码错误
    """
    status_code = 500
    error_code = 10008
    msg = 'Encode image error'


class ProcessImageException(ApiException):
    """
    图片处理错误
    """
    status_code = 500
    error_code = 10009
    msg = 'Process image error'


class Base64DecodeException(ApiException):
    """
    Base64解码错误
    """
    status_code = 400
    error_code = 10010
    msg = 'Base64 decode error'


class UrlDecodeException(ApiException):
    """
    UrlDecode解码错误
    """
    status_code = 400
    error_code = 10011
    msg = 'URL decode error'


class ResourceException(ApiException):
    """
    GPU/显存资源不足，服务临时不可用
    """
    status_code = 500
    error_code = 10012
    msg = 'URL decode error'


class SliceImageException(ApiException):
    """
    图片分块错误
    """
    status_code = 500
    error_code = 10013
    msg = 'Slice image error'


class MergeImageException(ApiException):
    """
    图片块合并错误
    """
    status_code = 500
    error_code = 10014
    msg = 'Merge image error'


class CallBackException(ApiException):
    """
    回调异常
    """
    status_code = 500
    error_code = 10015
    msg = 'Call back error'


class UnknownException(ApiException):
    """
    未知异常
    """
    status_code = 500
    error_code = 10024
    msg = 'Unknown error'

