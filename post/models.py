from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Category(models.Model):
    cname = models.CharField(max_length=30,unique=True,verbose_name='类别名称')

    class Meta:
        db_table = 't_caegory'
        verbose_name_plural = '分类'

    def __str__(self):
        return '分类：%s'%self.cname


class Tag(models.Model):
    tname = models.CharField(max_length=30,unique=True,verbose_name='标签名称')


    class Meta:
        db_table = 't_tag'
        verbose_name_plural = '标签'

    def __str__(self):
        return self.tname

class Post(models.Model):
    title = models.CharField(max_length=100,unique=True,verbose_name='标题')
    description = models.CharField(max_length=200,verbose_name='简介')
    content = RichTextUploadingField(null=True,blank=True)
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='分类')
    tag = models.ManyToManyField(Tag)

    class Meta:
        db_table = 't_post'
        verbose_name_plural = '帖子'

    def __str__(self):
        return '标题：%s' % self.title