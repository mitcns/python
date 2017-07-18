# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

# Create your views here.
from models import BlogPost, BlogPostForm
from django.http import HttpResponse, HttpResponseRedirect
# from django.template import RequestContext
from datetime import datetime

def myblog(request):
    posts = BlogPost.objects.all()[:10]
    return render(request, 'blog-list.html', {'posts': posts, 'form': BlogPostForm()})
    # return render_to_response('blog-list.html', {'posts': posts}, RequestContext(request)) TODO 此方法在新版中已改动

def index(request):
    return HttpResponse(u'你好啊，Django！')

def create_from(req): # TODO 逐个字段获取不符合 DRY 原则
    if req.method == 'POST':
        getData = req.POST.get
        BlogPost(
            title=getData('title'),
            body=getData('body'),
            timestamp=datetime.now()
        ).save()
    return HttpResponseRedirect('/blog/list/')

def create_model_form(req):
    if req.method == 'POST':
        form = BlogPostForm(req.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.timestamp = datetime.now()
            post.save()
    return HttpResponseRedirect('/blog/list/')
