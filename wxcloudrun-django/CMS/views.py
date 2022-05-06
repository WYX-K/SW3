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
from django.core.serializers import serialize
import logging
from .models import *
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
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
    isChecked = request.POST.get('isChecked')
    logger.info('Login Username: {}, Login PWD: {}'.format(username, pwd))

    users = UserInfo.objects.filter(username=username)
    if len(users) != 0:
        user = users[0]
        vertify_pwd = str(user.pwd).strip()
        if pwd == vertify_pwd:
            if user.role == 'uicer' and isChecked == 'false':
                sendMail(user.username, pwd)
                return HttpResponse(json.dumps({"res": "Send Email Success!"}, ensure_ascii=False), status=201)
            else:
                user_temp = {
                    "username": user.username,
                    "name": user.name,
                    "role": user.role,
                    "major": user.major
                }
                return HttpResponse(json.dumps(user_temp, ensure_ascii=False), status=200)
        else:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=500)


def sendMail(username, pwd):
    try:
        mail_msg = """
        <p> Hello, welcome to use Sigma CMS! </p>
        <p> Please check whether the following information is correct. 
        If you receive this email by mistake, please ignore it! </p>
        <p> Username: """ + username.split('@')[0] + """</p>
        <p> Please click the following link to activate your account: </p>
        <p> <a href="http://localhost:3000/login/?username="""+username+"""&pwd="""+pwd+"""">Activate</a></p>
        """
        mail('1135613552@qq.com', 'onvifnjypwxkjfde',
             username, 'WYX', 'uicer', mail_msg)
    except:
        print('邮件发送失败！')


'''
    配置发邮件所需的基础信息
    my_sender # 配置发件人邮箱地址***@qq.com
    my_pass   # 配置发件人邮箱密码 
    to_user   # 配置收件人邮箱地址***@163.com
    my_nick   # 配置发件人昵称草璧月
    to_nick   # 配置收件人昵称方立娇
    mail_msg  # 配置邮件内容你好，这是我用python发送的电子邮件
'''


def mail(my_sender, my_pass, to_user, my_nick, to_nick, mail_msg):
    # 必须将邮件内容做一次MIME转换--发送含链接的邮件
    msg = MIMEText(mail_msg, 'html', 'utf-8')
    # 配置发件人名称和邮箱地址
    msg['from'] = formataddr([my_nick, my_sender])
    # 配置收件人名称和邮箱地址
    msg['to'] = formataddr([to_nick, to_user])
    # 配置邮件主题
    msg['Subject'] = "Welcom to CMS"
    # 配置python与邮件的SMPT服务器的连接通道（ qq邮箱）
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    server.set_debuglevel(1)
    # 模拟登录
    server.login(my_sender, my_pass)
    # 邮件内容发送
    server.sendmail(my_sender, [to_user, ], msg.as_string())
    # 关闭连接通道
    server.quit()

###################################################
###################################################
# Post API
###################################################


'''
api: /poster
method: POST/GET/DELETE
param {username} request
return {posterdata}
'''


def poster(request):
    if request.method == 'POST' and request.POST:
        title = request.POST.get('title')
        author = request.POST.get('author')
        summary = request.POST.get('summary')
        file = request.FILES.get('file').read()
        major = request.POST.get('major')
        author_email = request.POST.get('author_email')
        
        res = Poster.objects.create(
            title=title, author=author, author_email=author_email, summary=summary, file=file, major=major)
        if res:
            return HttpResponse(json.dumps({"res": "success"}, ensure_ascii=False), status=200)
        else:
            return HttpResponse(json.dumps({"res": "fail"}, ensure_ascii=False), status=500)
    

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
