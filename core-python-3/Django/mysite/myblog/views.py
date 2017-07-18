# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

# Create your views here.
from models import BlogPost
from django.http import HttpResponse, HttpResponseRedirect
# from django.template import RequestContext
from datetime import datetime

def myblog(request):
    posts = BlogPost.objects.all()[:10]
    return render(request, 'blog-list.html', {'posts': posts})
    # return render_to_response('blog-list.html', {'posts': posts}, RequestContext(request)) TODO 此方法在新版中已改动

def index(request):
    return HttpResponse(u'你好啊，Django！')

def create_from(req):
    if req.method == 'POST':
        BlogPost(
            title=req.POST.get('title'),
            body=req.POST.get('body'),
            timestamp=datetime.now()
        ).save()
    return HttpResponseRedirect('/blog/list/')
