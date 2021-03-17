#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/3/15 13:57 
# @Author : TETE
# @File : search_indexes.py
from haystack import indexes

from post.models import Post

#注意格式（模型类名+Index）
class PostIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True)

    #给title，content 设置索引
    title = indexes.NgramField(model_attr='title')
    content = indexes.NgramField(model_attr='content')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-create_time')
