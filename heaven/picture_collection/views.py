from django.http import HttpResponse
from rest_framework.response import Response

from common.api_view import APIView
from .mongo_ import CommonImagesMongodb


# Create your views here.


class UpdateImageView(APIView):
    def put(self, request, *args, **kwargs):
        image = self.request.FILES.get('img')
        data = self.request.data
        set_data = {
            "name": data['name'],
            "img": image,
            "url": data['url']
        }

        try:
            CommonImagesMongodb.objects.create(**set_data)
        except Exception as e:
            print(str(e))
        return Response(self.msg(code=200, msg="成功"))


class GetImageView(APIView):
    def get(self, request, *args, **kwargs):
        all_image = CommonImagesMongodb.objects.all()
        img = all_image[0].img.read()
        return HttpResponse(img, content_type="image/png")
