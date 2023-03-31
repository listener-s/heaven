from django.urls import re_path

from .views import *

urlpatterns = [
    re_path(r'^set/image/$', UpdateImageView.as_view()),
    re_path(r'^image/$', GetImageView.as_view()),
]
