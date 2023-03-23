from django.contrib import admin

from .models import BackupAccountNumber, BackupWebUrl

# Register your models here.

admin.site.register(BackupAccountNumber)
admin.site.register(BackupWebUrl)
