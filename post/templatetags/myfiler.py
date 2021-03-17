#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/3/11 9:58 
# @Author : TETE
# @File : myfiler.py
from bs4 import BeautifulSoup
from django.template import Library
from markdown.extensions import Extension

from post.models import Post
from post.templatetags import mdextension

register = Library()

@register.filter
def md(value):
    import markdown
    configs = {}
    myext = mdextension.CodeExtension(configs=configs)
    md = markdown.markdown(value, extensions=[myext])
    return md

@register.filter
def getPic(postid:int):

    c = Post.objects.values('content').filter(id=postid)
    c= str(c)
    soup = BeautifulSoup(c, 'html.parser')
    if soup.img:
        src =soup.img['src']
        return src

    return ''




