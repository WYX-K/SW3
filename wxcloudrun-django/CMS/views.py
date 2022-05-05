'''
Author: Simon
Date: 2022-04-12 17:43:00
LastEditTime: 2022-05-03 20:05:53
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /wxcloudrun-django/CMS/views.py
'''
from collections import UserList
import json
from django.http import HttpResponse
import logging
from .models import *
import random

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
            return HttpResponse(json.dumps(p_temp, ensure_ascii=False), status=200)
        else:
            return HttpResponse(status=404)

    return HttpResponse(status=500)


###################################################
###################################################
# Vote API
###################################################

'''
api: /vote
method: POST/GET
param {username} request
return {posterdata}
'''


def vote(request):
    if request.method == 'GET' and request.GET:
        data = []
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
                    data.append(p_temp)
            else:
                for poster in poster_queryset:
                    p_temp = {
                        "posterid": None,
                    }
                    data.append(p_temp)

        return HttpResponse(json.dumps(data, ensure_ascii=False), status=200)
    elif request.method == 'POST' and request.POST:
        vote_posterid = request.POST.get('posterid')
        voteuname = request.POST.get('voteuname')

        logger.info('Voted Poster ID: {}, Voter Name: {}'.format(
            vote_posterid, voteuname))

        if vote_posterid and voteuname:
            poster_queryset = Poster.objects.filter(posterid=vote_posterid)
            if poster_queryset:
                return HttpResponse(json.dumps({"res": "Success!"}, ensure_ascii=False), status=200)
            else:
                return HttpResponse(json.dumps({"res": "Failed!"}, ensure_ascii=False), status=401)
        else:
            return HttpResponse(json.dumps({"res": "Parameters Not Completed!"}, ensure_ascii=False), status=404)
    return HttpResponse(status=500)

###################################################
###################################################
# Lucky Draw API
###################################################


'''
api: /chooseLuckydraw
description: choose luckydraw
param {} request
return {name, rank}
'''


def chooseLuckydraw(request):
    data = []
    user_queryset = UserInfo.objects.all()
    user_list = []

    # get all username
    for user in user_queryset:
        user_list.append(user.username)
    user_len = len(user_list)

    # get random num
    rank1_num = random.randint(0, user_len - 1)
    rank1_user = user_list[rank1_num]
    rank2_num = random.randint(0, user_len - 1)
    while rank1_num == rank2_num:
        rank2_num = random.randint(0, user_len - 1)
    rank2_user = user_list[rank2_num]
    rank3_num = random.randint(0, user_len - 1)
    while rank3_num == rank1_num or rank3_num == rank2_num:
        rank3_num = random.randint(0, user_len - 1)
    rank3_user = user_list[rank3_num]

    p_temp = {
        "First": rank1_user,
        "Second": rank2_user,
        "Third": rank3_user
    }
    data.append(p_temp)

    return HttpResponse(json.dumps({"status": 200, "msg": "OK!", "data": data}, ensure_ascii=False))
