from rest_framework import generics
from rest_framework.views import APIView


class ViewCommon:

    @classmethod
    def msg(cls, code, msg=None, data=None, **kwargs):
        result = dict()
        result['code'] = int(code) if str(code).isdigit() else 50000
        result['mag'] = kwargs.get('remsg', None) or msg
        if data is not None:
            result['data'] = data
        return result


class APIView(APIView, ViewCommon):
    pass


class GenericAPIView(generics.GenericAPIView, ViewCommon):
    pass


class CreateAPIView(generics.CreateAPIView, ViewCommon):
    pass


class ListAPIView(generics.ListAPIView, ViewCommon):
    pass


class RetrieveAPIView(generics.RetrieveAPIView, ViewCommon):
    pass


class DestroyAPIView(generics.DestroyAPIView, ViewCommon):
    pass


class UpdateAPIView(generics.UpdateAPIView, ViewCommon):
    pass


class ListCreateAPIView(generics.ListCreateAPIView, ViewCommon):
    pass


class RetrieveUpdateAPIView(generics.RetrieveUpdateAPIView, ViewCommon):
    pass


class RetrieveDestroyAPIView(generics.RetrieveDestroyAPIView, ViewCommon):
    pass


class RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView, ViewCommon):
    pass
