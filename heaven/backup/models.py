from django.db import models

from account.models import User


# Create your models here.


class BackupAccountNumber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='创建人')
    app_name = models.CharField(max_length=255, verbose_name="app ｜ 网站 /名称", null=True, blank=True)
    app_user_name = models.CharField(max_length=255, verbose_name="app ｜ 网站 /用户名", null=True, blank=True)
    app_user_password = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'Backup_Account_Number_Model'
        verbose_name = "备份表"
        verbose_name_plural = "备份列表"

    def __str__(self):
        return self.app_name


class BackupWebUrl(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='创建人')
    url = models.CharField(max_length=255, null=True, blank=True)
    url_name = models.CharField(max_length=255, null=True, blank=True)
    url_remarks = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'Backup_Web_Url'
        verbose_name = "备份网站表"
        verbose_name_plural = "备份网站列表"

    def __str__(self):
        return self.url_name
