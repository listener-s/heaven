from rest_framework.views import exception_handler

from common.reptile import Reptile


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)  # 获取本来应该返回的exception的response
    if response is not None:
        response.data['status_code'] = response.status_code
        for exces in response.data:
            if isinstance(response.data.get(exces), list):
                response.data.get(exces)[0] = Reptile.chinese_translate(response.data.get(exces)[0])
    print('中文报错：', Reptile.chinese_translate(str(exc)))
    return response
