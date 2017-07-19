# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
# todo 单元测试还挺有意思的
from datetime import datetime
from django.test.client import Client
from models import BlogPost

class BlogPostTest(TestCase):

    def test_obj_create(self):
        BlogPost.objects.create(
            title='raw title',
            body='raw body',
            timestamp=datetime.now()
        )
        self.assertEqual(1, BlogPost.objects.count())
        self.assertEqual('raw title', BlogPost.objects.get(id=1).title)

    def test_home(self):
        res = self.client.get('/blog/')
        self.failUnlessEqual(res.status_code, 200)

    def test_slash(self):
        res = self.client.get('/')
        self.assertIn(res.status_code, (200, 301, 302))

    def test_empty(self):
        res = self.client.get('/blog/create/')
        self.assertIn(res.status_code, (301, 302))

    def test_post_create(self):
        res = self.client.post('/blog/create/', {
            'title': 'post title',
            'body': 'post body',
        })
        self.assertIn(res.status_code, (301, 302))
        self.assertEqual(1, BlogPost.objects.count())
        self.assertEqual('post title', BlogPost.objects.get(id=2).title)

