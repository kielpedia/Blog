'''
Created on Aug 13, 2011

@author: kiel
'''
from django.conf.urls.defaults import patterns
from django.views.generic import ListView, DetailView
from Loysen.blog.views import BlogView, BlogPostView
from Loysen.blog.models import Post


urlpatterns = patterns('blog.views',
    (r'^$',
        BlogView.as_view()),
    (r'^(?P<pk>\d+)/$',
        BlogPostView.as_view()),
)
