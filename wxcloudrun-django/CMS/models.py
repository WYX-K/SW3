'''
Author: Simon
Date: 2022-04-12 17:43:00
LastEditTime: 2022-05-03 19:12:46
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /wxcloudrun-django/CMS/models.py
'''
# from os import major
from django.db import models

# Create your models here.

'''
    User Table
'''


class UserInfo(models.Model):
    username = models.CharField("Username", max_length=100, default="")
    pwd = models.CharField("Password", max_length=100, default="")
    role = models.CharField("Role", max_length=100, default="")
    major = models.CharField("Major", max_length=100, default="")
    name = models.CharField("Name", max_length=100, default="")

    class Meta:
        verbose_name = "UserInfo"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


'''
    UICer Poster Table
'''


class UICerPoster(models.Model):
    username = models.CharField("Username", max_length=100, default="")
    posterid = models.IntegerField("Poster ID", default=0)
    luckydraw = models.CharField("Lucky Draw", max_length=100, default="")

    class Meta:
        verbose_name = "UICerPoster"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


'''
    Poster Table
'''


class Poster(models.Model):
    title = models.CharField("Title", max_length=500, default="")
    summary = models.CharField("Summary", max_length=1000, default="")
    file = models.BinaryField("File")
    major = models.CharField("Major", max_length=100, default="")
    author = models.CharField("Author", max_length=100, default="")
    author_email = models.CharField("Username", max_length=100, default="")
    voteNum = models.IntegerField("Vote Num", default=0)
    grade = models.FloatField("Grade", default=0.0)

    class Meta:
        verbose_name = "Poster"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


'''
    Judge Poster
'''


class JudgePoster(models.Model):
    judge = models.CharField("Judge", max_length=1000, default="")
    poster = models.CharField("Poster", max_length=1000, default="")
    visual_layout = models.CharField(
        "Visual Layout", max_length=100, default="")
    poster_organization = models.FloatField("Poster Organization", default=0.0)
    poster_content = models.FloatField("Poster Content", default=0.0)
    written_language = models.FloatField("Written Language", default=0.0)
    oral_presentation = models.FloatField("Oral Presentation", default=0.0)
    average = models.FloatField("Average", default=0.0)

    class Meta:
        verbose_name = "JudgePoster"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.poster


'''
    Head Poster
'''


class HeadPoster(models.Model):
    poster = models.CharField("Poster", max_length=1000, default="")
    judge = models.CharField("Judge", max_length=1000, default="")
    visual_layout = models.CharField(
        "Visual Layout", max_length=100, default="")
    poster_organization = models.FloatField("Poster Organization", default=0.0)
    poster_content = models.FloatField("Poster Content", default=0.0)
    written_language = models.FloatField("Written Language", default=0.0)
    oral_presentation = models.FloatField("Oral Presentation", default=0.0)

    class Meta:
        verbose_name = "HeadPoster"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.poster


class Rules(models.Model):
    num_headjudge = models.IntegerField("Num Head Judges", default=2)
    num_judges = models.IntegerField("Num Judges", default=14)
    num_firstprize = models.IntegerField("Num First Prize", default=1)
    num_secondprize = models.IntegerField("Num Second Prize", default=1)
    num_thirdprize = models.IntegerField("Num Third Prize", default=1)

    class Meta:
        verbose_name = "Rules"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.num_headjudge


class Conference(models.Model):
    date = models.CharField("Date", max_length=100, default="")
    time = models.CharField("Time", max_length=100, default="")
    content = models.CharField("Content", max_length=1000, default="")

    class Meta:
        verbose_name = "Conference"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.date
