# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

# Create your views here.
from models import BlogPost
from django.http import HttpResponse

def myblog(request):
    posts = BlogPost.objects.all()[:10]
    return render(request, 'blog-list.html', {'posts': posts})
    # return render_to_response('blog-list.html', {'posts': posts})

def index(request):
    return HttpResponse(u'你好啊，Django！')
