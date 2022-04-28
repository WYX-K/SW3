'''
Author: Simon
Date: 2022-04-12 17:43:00
LastEditTime: 2022-04-29 00:23:51
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /wxcloudrun-django/CMS/views.py
'''
import json
from django.http import HttpResponse
import logging
from .models import *

# Create your views here.

logger = logging.getLogger('log')

###################################################
###################################################
# User API
###################################################

'''
api: /login
description: login
param {username, pwd} request
return {username, role, name, major} 
'''
def logIn(request):
    # test
    # username = request.GET.get('username')
    # pwd = request.GET.get('pwd')
    
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    
    logger.info('Login Username: {}, Login PWD: {}'.format(username, pwd))
    
    queryset = UserInfo.objects.filter(username=username)
    for q in queryset:
        vertify_pwd = str(q.pwd).strip()
        if pwd == vertify_pwd:
            p_temp = {
                "name": q.username,
                "role": q.role,
                "major": q.major
            }
            return HttpResponse(json.dumps({"status": 200, "msg": "OK!", "Login":True, "data": p_temp}, ensure_ascii=False))
        else:
            return HttpResponse(json.dumps({"status": 404, "msg": "NO!", "Login":False}, ensure_ascii=False))
    
    return HttpResponse(json.dumps({"status": 500, "msg": "Err!", "Login":False}, ensure_ascii=False))


###################################################
###################################################
# Vote API
###################################################

'''
api: /vote
description: get vote which one
param {username} request
return {posterid}
'''
def vote(request):
    username = request.GET.get('username')
    
    uicerposter_queryset = UICerPoster.objects.filter(username=username)
    for uicerposter in uicerposter_queryset:
        verified_posterid = uicerposter.posterid
        poster_queryset = Poster.objects.filter(posterid=verified_posterid)
        if poster_queryset:
            for poster in poster_queryset:
                p_temp = {
                    "posterid": poster.posterid,
                }
        else:
            for poster in poster_queryset:
                p_temp = {
                    "posterid": None,
                }
                
    return HttpResponse(json.dumps({"status": 200, "msg": "OK!", "data": p_temp}, ensure_ascii=False))
    
