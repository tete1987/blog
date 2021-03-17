import math

from bs4 import BeautifulSoup
from django.shortcuts import render

# Create your views here.

#渲染主页面
from post.models import Post
from django.core.paginator import Paginator

def queryAll(request,num=1):

    # num = request.GET.get('num',1)
    num = int(num)
    #获取所有帖子信息
    post_list = Post.objects.all().order_by('-create_time')


    #创建分页器对象
    pageObj =Paginator(post_list,2)

    #获取当前页的数据
    perPageList = pageObj.page(num)

    #生成页码的列表
    # 每页开始页码
    begin = (num - int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1
    # 每页结束页码
    end = begin + 9
    if end > pageObj.num_pages:
        end = pageObj.num_pages

    if end <= 10:
        begin = 1
    else:
        begin = end - 9

    pageList = range(begin, end + 1)


    return render(request, 'index.html', {'post_list':perPageList, 'pageList':pageList, 'currentNum':num})

#阅读全文
def postDetail(request,postid):
    postid = int(postid)

    #根据postid 查询帖子的详情信息
    post = Post.objects.get(id=postid)


    return render(request,'detail.html',{'post':post})

def getPic(postid):
    postid = int(postid)
    content = Post.objects.values('content').filter(id=postid)
    content= str(content)
    soup = BeautifulSoup(content, "lxml")
    src = soup.img['src']
    return src

#根据类别id查询所有帖子
def queryPostByCid(request,cid):
    postList = Post.objects.filter(category_id=cid)

    return render(request,'article.html',{'postList':postList})

#根据发帖时间查询所有帖子
def queryPostByCreateTime(request,year,month):
    postList = Post.objects.filter(create_time__year=year,create_time__month=month)

    return render(request,'article.html',{'postList':postList})