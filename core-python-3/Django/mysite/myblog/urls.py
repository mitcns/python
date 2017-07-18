# !/usr/bin/env python
# coding=utf-8

from django.conf.urls import url, include
import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^list/', views.myblog, name='blog'),
    url(r'^index/' or r'^$', views.index, name='index'),
    url(r'^create/', views.create_model_form, name='create')
]