'''
Author: Simon
Date: 2022-04-12 17:43:00
LastEditTime: 2022-04-12 17:48:12
LastEditors: Simon
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /wxcloudrun-django/CMS/admin.py
'''
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserInfo)  # register UserInfo Table
