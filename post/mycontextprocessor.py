#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/3/11 16:03 
# @Author : TETE
# @File : mycontextprocessor.py

from django.db.models import Count

from post.models import Post


def getRightInfo(request):
    #1.获取分类信息
    r_catepost = Post.objects.values('category__cname','category').annotate(c=Count('*')).order_by('-c')

    #2.获取近期文章
    r_report = Post.objects.all().order_by('-create_time')[:3]

    #3.获取日期归档信息
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("select create_time,count('*')  c from t_post GROUP BY DATE_FORMAT(create_time,'%Y-%m') order by c desc,create_time desc ")
    r_filepost =cursor.fetchall()


    return {'r_catepost':r_catepost,'r_report':r_report,'r_filepost':r_filepost}

