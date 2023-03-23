from rest_framework.views import exception_handler

from .translates import TranslateCommon


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)  # 获取本来应该返回的exception的response
    if response is not None:
        response.data['status_code'] = response.status_code
        for response_info in response.data:
            if isinstance(response.data.get(response_info), list):
                response.data.get(response_info)[0] = TranslateCommon.chinese_translate(
                    response.data.get(response_info)[0])
    print('中文报错：', TranslateCommon.chinese_translate(str(exc)))
    return response
