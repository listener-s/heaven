from django.db import models


# Create your models here.


class Cartoon(models.Model):
    is_del = models.BooleanField(default=False)
    cartoon_name = models.CharField(max_length=255, blank=True, null=True)
    mongo_name = models.CharField(max_length=255, blank=True, null=True)
