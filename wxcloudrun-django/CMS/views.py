'''
Author: Simon
Date: 2022-04-12 17:43:00
LastEditTime: 2022-05-03 20:05:53
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /wxcloudrun-django/CMS/views.py
'''
import base64
import json
from django.http import HttpResponse, QueryDict
import logging
from .models import *
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from django.db.models import Q
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
            return HttpResponse(json.dumps({"res": "fail"}, ensure_ascii=False), status=404)
    return HttpResponse(json.dumps({"res": "fail"}, ensure_ascii=False), status=404)


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
'''


def poster(request):
    if request.method == 'POST' and request.POST:
        title = request.POST.get('title')
        author = request.POST.get('author')
        summary = request.POST.get('summary')
        file = request.FILES.get('file').read()
        major = request.POST.get('major')
        author_email = request.POST.get('author_email')
        if len(Poster.objects.filter(author_email=author_email)) == 0:
            res = Poster.objects.create(
                title=title, author=author, author_email=author_email, summary=summary, file=file, major=major)
            if res:
                return HttpResponse(json.dumps({"res": "success"}, ensure_ascii=False), status=200)
    elif request.method == "DELETE":
        qs = QueryDict(request.body)
        ids = qs.getlist('ids[]')
        for id in ids:
            Poster.objects.filter(id=id).delete()
        return HttpResponse(json.dumps({"res": "success"}, ensure_ascii=False), status=200)
    elif request.method == 'GET' and request.GET:
        pageNum = int(request.GET.get('pageNum'))
        pageSize = int(request.GET.get('pageSize'))
        num = pageNum * pageSize
        major = request.GET.get('major')
        if major == 'all':
            posters = Poster.objects.all()
            total = len(posters)
            posters = posters[num:num+pageSize]
        elif major == 'DST':
            posters = Poster.objects.all()
            isAllGraded = True
            for poster in posters:
                if poster.grade == 0:
                    isAllGraded = False
                    break
            if isAllGraded:
                posters_major = Poster.objects.values(
                    'major').order_by('major').distinct()
                data = []
                for poster_major in posters_major:
                    major = poster_major.get('major')
                    posters = Poster.objects.filter(
                        major=major).order_by('-grade')
                    temp = {}
                    temp['id'] = posters[0].id
                    temp['title'] = posters[0].title
                    temp['author'] = posters[0].author
                    temp['author_email'] = posters[0].author_email
                    temp['summary'] = posters[0].summary
                    temp['major'] = posters[0].major
                    url = str(base64.b64encode(posters[0].file), 'utf8')
                    temp['url'] = url
                    data.append(temp)
                return HttpResponse(json.dumps(data, ensure_ascii=False), status=200)
            return HttpResponse(json.dumps({"res": "no data"}, ensure_ascii=False), status=201)
        else:
            posters = Poster.objects.filter(major=major)
            total = len(posters)
            posters = posters[num:num+pageSize]

        res = []
        for poster in posters:
            data = {}
            data['id'] = poster.id
            data['title'] = poster.title
            data['author'] = poster.author
            data['summary'] = poster.summary
            url = str(base64.b64encode(poster.file), 'utf8')
            data['url'] = url
            data['major'] = poster.major
            data['total'] = total
            res.append(data)
        return HttpResponse(json.dumps(res, ensure_ascii=False), status=200)
    return HttpResponse(json.dumps({"res": "fail"}, ensure_ascii=False), status=500)


'''
api: /editPoster
method: POST
'''


def editPoster(request):
    title = request.POST.get('title')
    author = request.POST.get('author')
    summary = request.POST.get('summary')
    file = request.FILES.get('file')
    major = request.POST.get('major')
    author_email = request.POST.get('author_email')
    id = request.POST.get('id')
    poster = Poster.objects.get(id=id)
    if title:
        poster.title = title
    if author:
        poster.author = author
    if summary:
        poster.summary = summary
    if file:
        poster.file = file.read()
    if major:
        poster.major = major
    if author_email:
        poster.author_email = author_email
    poster.save()
    return HttpResponse(json.dumps({"res": "success"}, ensure_ascii=False), status=200)


###################################################
###################################################
# Vote API
###################################################
'''
api: /vote
method: POST/GET
'''


def vote(request):
    if request.method == 'GET' and request.GET:
        username = request.GET.get('username')
        uicer = UICerPoster.objects.filter(username=username)
        if len(uicer):
            poster_id = uicer[0].posterid
            poster = Poster.objects.get(id=poster_id)
            data = {}
            data['title'] = poster.title
            data['author'] = poster.author
            data['major'] = poster.major
            return HttpResponse(json.dumps(data, ensure_ascii=False), status=200)
        else:
            return HttpResponse(status=201)
    elif request.method == 'POST' and request.POST:
        poster_id = request.POST.get('posterid')
        voteuname = request.POST.get('username')
        uicer = UICerPoster.objects.filter(username=voteuname)
        if len(uicer):
            p_poster = Poster.objects.get(id=uicer[0].posterid)
            p_poster.voteNum -= 1
            p_poster.save()
            uicer[0].posterid = poster_id
            uicer[0].save()
        else:
            UICerPoster.objects.create(username=voteuname, posterid=poster_id)
        poster = Poster.objects.get(id=poster_id)
        poster.voteNum += 1
        poster.save()
        return HttpResponse(json.dumps({"res": "success"}, ensure_ascii=False), status=200)
    return HttpResponse(json.dumps({"res": "fail"}, ensure_ascii=False), status=500)

###################################################
###################################################
# Lucky Draw API
###################################################


'''
api: /luckydraw
method: POST/GET
'''


def luckydraw(request):
    if request.method == 'POST':
        user_queryset = UICerPoster.objects.all()
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
        uicer = UICerPoster.objects.get(username=rank1_user)
        uicer.luckydraw = 'FIRST'
        uicer.save()
        uicer = UICerPoster.objects.get(username=rank2_user)
        uicer.luckydraw = 'SECOND'
        uicer.save()
        uicer = UICerPoster.objects.get(username=rank3_user)
        uicer.luckydraw = 'THIRD'
        uicer.save()
        data = {
            "1": rank1_user,
            "2": rank2_user,
            "3": rank3_user
        }
        return HttpResponse(json.dumps(data, ensure_ascii=False), status=200)
    elif request.method == 'GET':
        uicers = UICerPoster.objects.filter(
            Q(luckydraw='FIRST') | Q(luckydraw='SECOND') | Q(luckydraw='THIRD'))
        if len(uicers):
            data = []
            for uicer in uicers:
                temp = {}
                temp['name'] = UserInfo.objects.get(
                    username=uicer.username).name
                temp['username'] = uicer.username
                temp['luckydraw'] = uicer.luckydraw
                data.append(temp)
            return HttpResponse(json.dumps(data, ensure_ascii=False), status=200)
        else:
            return HttpResponse(status=201)
    return HttpResponse(json.dumps({"res": "fail"}, ensure_ascii=False), status=500)


###################################################
###################################################
# Grade API
###################################################


'''
api: /grade
method: POST/GET
'''


def grade(request):
    if request.method == 'POST' and request.POST:
        judgename = request.POST.get('judgename')
        role = request.POST.get('role')
        posterid = request.POST.get('id')
        visual_layout = float(request.POST.get('visual_layout'))
        poster_organization = float(request.POST.get('poster_organization'))
        poster_content = float(request.POST.get('poster_content'))
        written_language = float(request.POST.get('written_language'))
        oral_presentation = float(request.POST.get('oral_presentation'))
        aver = (visual_layout + poster_organization +
                poster_content + written_language + oral_presentation) / 5
        if role == 'judge':
            judgeposters = JudgePoster.objects.filter(
                Q(judge=judgename) & Q(poster=posterid))
            if len(judgeposters) != 0:
                judgeposters.delete()
            JudgePoster.objects.create(average=aver, judge=judgename, poster=posterid, visual_layout=visual_layout, poster_content=poster_content,
                                       poster_organization=poster_organization, written_language=written_language, oral_presentation=oral_presentation)
            judgeposters = JudgePoster.objects.filter(poster=posterid)
            if len(judgeposters) == 2:
                aver = (judgeposters[0].average + judgeposters[1].average) / 2
                poster = Poster.objects.get(id=posterid)
                poster.grade = aver
                poster.save()
        elif role == 'head_judge':
            headposters = HeadPoster.objects.filter(
                Q(judge=judgename) & Q(poster=posterid))
            if len(headposters) != 0:
                headposters.delete()
            HeadPoster.objects.create(judge=judgename, poster=posterid, visual_layout=visual_layout, poster_content=poster_content,
                                      poster_organization=poster_organization, written_language=written_language, oral_presentation=oral_presentation)
        return HttpResponse(json.dumps({"res": "success"}, ensure_ascii=False), status=200)
    if request.method == 'GET' and request.GET:
        judgename = request.GET.get('judgename')
        role = request.GET.get('role')
        if role == 'judge':
            judgeposters = JudgePoster.objects.filter(judge=judgename)
        else:
            judgeposters = HeadPoster.objects.filter(judge=judgename)
        if len(judgeposters) != 0:
            data = []
            for judgeposter in judgeposters:
                data.append(judgeposter.poster)
            return HttpResponse(json.dumps(data, ensure_ascii=False), status=200)
        return HttpResponse(status=201)
    return HttpResponse(json.dumps({"res": "fail"}, ensure_ascii=False), status=500)
