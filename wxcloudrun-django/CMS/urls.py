'''
Author: Simon
Date: 2022-04-26 00:06:14
LastEditTime: 2022-05-03 19:52:44
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /wxcloudrun-django/wxcloudrun/urls.py
'''
"""wxcloudrun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from CMS import views as CMSviews
urlpatterns = (
    path('admin/', admin.site.urls),
    url(r'login', CMSviews.logIn),
    url(r'vote', CMSviews.vote),
    url(r'chooseLuckydraw', CMSviews.chooseLuckydraw),
    url(r'poster', CMSviews.poster),
    url(r'editPoster', CMSviews.editPoster),
)
