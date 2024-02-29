# DRF自带的视图异常处理类
from rest_framework.views import exception_handler
# 数据库异常处理类
from django.db import DatabaseError
from redis import RedisError
# 响应
from rest_framework.response import Response
from rest_framework import status

import logging

logging = logging.getLogger("django")


def custom_exception_handler(exc, context):
    """
        自定义异常处理
       :param exc: 异常类
       :param context: 抛出异常的上下文
       :return: Response响应对象
    """
    # 调用drf框架原生的异常处理方法，有异常返回异常，识别不了的返回None
    response = exception_handler(exc, context)
    # 如果通过drf的异常
    if response is None:
        view = context["view"]
        # 判断各种异常
        if isinstance(exc, DatabaseError):
            # 数据库异常
            # 记录到日志中
            logging.error(f"mysql数据库异常{view} {exc}")
            # 返回错误
            response = Response({"message", "服务器内部错误"}, status=status.HTTP_507_INSUFFICIENT_STORAGE)
        elif isinstance(exc, RedisError):
            logging.error(f"redis数据库异常{view} {exc}")
            # 返回错误
            response = Response({"message", "服务器内部错误"}, status=status.HTTP_507_INSUFFICIENT_STORAGE)

    return response
