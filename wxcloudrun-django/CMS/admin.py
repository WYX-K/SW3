'''
Author: Simon
Date: 2022-04-12 17:43:00
LastEditTime: 2022-04-28 00:19:11
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /wxcloudrun-django/CMS/admin.py
'''
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserInfo)  # register UserInfo Table
admin.site.register(UICerPoster)  # register UICerPoster Table
admin.site.register(Poster)  # register Poster Table
admin.site.register(PrePoster)  # register PrePoster Table
admin.site.register(JudgePoster)  # register JudgePoster Table
admin.site.register(HeadPoster)  # register HeadPoster Table

