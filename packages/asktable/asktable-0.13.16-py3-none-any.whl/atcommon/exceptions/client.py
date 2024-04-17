import inspect
import sys
from atcommon.exceptions.server import *


class ClientBaseError(Exception):
    code = 9
    message = "Client Error"


class ServerConnectionError(ClientBaseError):
    code = 9000
    message = "Server Connection Error"


class ServerError(ClientBaseError):
    # 无法解析返回的数据，未知的服务器错误
    code = 9001
    message = "Server Error"


class UnknownServerError(ClientBaseError):
    # 服务器返回了错误码，但client端无法识别
    code = 9002
    message = "Unknown Server Error"


class UploadFileError(ClientBaseError):
    code = 9003
    message = "Upload File Error"


class UnsupportedFileType(ClientBaseError):
    code = 9004
    message = "Unsupported File Type"


class DataSourceMetaProcessError(ClientBaseError):
    code = 9005
    message = "Datasource Meta Process Error"


class DataSourceMetaProcessTimeout(ClientBaseError):
    code = 9006
    message = "Datasource Meta Process Timeout"


def get_exception_by_code(code):
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            if getattr(obj, 'code') == code:
                return obj
    return None


def raise_exception_by_code(code, message):
    ex = get_exception_by_code(code)
    if ex:
        raise ex(message)
    else:
        raise UnknownServerError(f"Unknown error code: {code} {message}")
