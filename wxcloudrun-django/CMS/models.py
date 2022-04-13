'''
Author: Simon
Date: 2022-04-12 17:43:00
LastEditTime: 2022-04-12 18:05:37
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /wxcloudrun-django/CMS/models.py
'''
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    userid = models.IntegerField("User ID", default=1)
    username = models.CharField("Username", max_length=20, default="")
    pwd = models.CharField("pwd", max_length=100, default="")

    class Meta:
        verbose_name = "UserInfo"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username
    