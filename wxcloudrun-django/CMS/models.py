'''
Author: Simon
Date: 2022-04-12 17:43:00
LastEditTime: 2022-05-03 19:12:46
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /wxcloudrun-django/CMS/models.py
'''
from os import major
from django.db import models

# Create your models here.

'''
    User Table
'''
class UserInfo(models.Model):
    userid = models.IntegerField("User ID", default=1)
    username = models.CharField("Username", max_length=20, default="")
    pwd = models.CharField("Password", max_length=100, default="")
    role = models.CharField("Role", max_length=100, default="")
    major = models.CharField("Major", max_length=100, default="")

    class Meta:
        verbose_name = "UserInfo"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username

'''
    UICer Poster Table
'''
class UICerPoster(models.Model):
    username = models.CharField("Username", max_length=20, default="")
    posterid = models.IntegerField("Poster ID", default=0)
    luckydraw = models.CharField("Lucky Draw", max_length=100, default="")
    voteStatus = models.IntegerField("Vote Status", default=0)

    class Meta:
        verbose_name = "UICerPoster"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username
    
'''
    Poster Table
'''
class Poster(models.Model):
    posterid = models.IntegerField("Poster ID", default=0)
    title = models.CharField("Title", max_length=500, default="")
    summary = models.CharField("Summary", max_length=1000, default="")
    file = models.CharField("File", max_length=1000, default="")
    major = models.CharField("Major", max_length=100, default="")
    isGraded = models.IntegerField("IsGraded", default=0)
    voteNum = models.IntegerField("Vote Num", default=0)
    grade = models.IntegerField("Grade", default=0)
    
    class Meta:
        verbose_name = "Poster"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
    
'''
    Pre Poster Table
'''
class PrePoster(models.Model):
    username = models.CharField("Username", max_length=20, default="")
    posterid = models.IntegerField("Poster ID", default=0)
    
    class Meta:
        verbose_name = "PrePoster"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username

'''
    Judge Poster
'''
class JudgePoster(models.Model):
    username = models.CharField("Username", max_length=20, default="")
    poster = models.CharField("Poster", max_length=1000, default="")
    visual_layout = models.CharField("Visual Layout", max_length=100, default="")
    poster_organization = models.FloatField("Poster Organization", default=0.0)
    poster_content = models.FloatField("Poster Content", default=0.0)
    written_language = models.FloatField("Written Language", default=0.0)
    oral_presentation = models.FloatField("Oral Presentation", default=0.0)
    
    class Meta:
        verbose_name = "JudgePoster"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.poster
    
'''
    Head Poster
'''
class HeadPoster(models.Model):
    username = models.CharField("Username", max_length=20, default="")
    poster = models.CharField("Poster", max_length=1000, default="")
    visual_layout = models.CharField("Visual Layout", max_length=100, default="")
    poster_organization = models.FloatField("Poster Organization", default=0.0)
    poster_content = models.FloatField("Poster Content", default=0.0)
    written_language = models.FloatField("Written Language", default=0.0)
    oral_presentation = models.FloatField("Oral Presentation", default=0.0)
    
    class Meta:
        verbose_name = "HeadPoster"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.poster