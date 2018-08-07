class AzkabanClientException(Exception):
    """通用异常"""
    pass


class UndefinedAjaxApiException(AzkabanClientException):
    """未定义AJAX接口异常，不存在对应的AJAX接口"""
    pass


class IncorrectHttpMethodException(AzkabanClientException):
    """指定HTTP方法异常"""
    pass


class IncorrectParamException(AzkabanClientException):
    """参数错误异常"""
    pass


class CallbackException(IncorrectParamException):
    """回调异常，回调参数有误，无法执行回调函数"""
    pass
