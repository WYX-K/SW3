'''
Author: Simon
Date: 2022-04-12 17:43:00
LastEditTime: 2022-04-26 00:45:06
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /wxcloudrun-django/CMS/views.py
'''
import json
from django.http import HttpResponse
from django.shortcuts import render
import logging
from .models import UserInfo

# Create your views here.

logger = logging.getLogger('log')

# api: /login
def logIn(request):
    # test
    # username = request.GET.get('username')
    # pwd = request.GET.get('pwd')
    data = []
    
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    
    logger.info('Login Username: {}, Login PWD: {}'.format(username, pwd))
    
    queryset = UserInfo.objects.filter(username=username)
    for q in queryset:
        vertify_pwd = str(q.pwd).strip()
        if pwd == vertify_pwd:
            p_temp = {
                "name": q.username,
                "role": q.role
            }
            data.append(p_temp)
            return HttpResponse(json.dumps({"status": 200, "msg": "OK!", "Login":True, "data": p_temp}, ensure_ascii=False))
        else:
            return HttpResponse(json.dumps({"status": 404, "msg": "NO!", "Login":False}, ensure_ascii=False))
    
    return HttpResponse(json.dumps({"status": 500, "msg": "Err!", "Login":False}, ensure_ascii=False))
    