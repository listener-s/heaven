from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=40)
    iphone = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=15)

    class Meta:
        db_table = 'User_Model'
        verbose_name = "用户表"
        verbose_name_plural = "用户列表"

    def __str__(self):
        return self.username
