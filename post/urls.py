#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/3/9 14:03 
# @Author : TETE
# @File : urls.py
from django.urls import path, re_path

from post import views

urlpatterns = [
    path('', views.queryAll),
    re_path('page/(\d+)$',views.queryAll),
    re_path('post/(\d+)$',views.postDetail),
    re_path('category/(\d+)$',views.queryPostByCid),
    re_path('archive/(\d+)/(\d+)$',views.queryPostByCreateTime)

]
