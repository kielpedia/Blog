'''
Created on Aug 13, 2011

@author: kiel
'''
from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.defaults import patterns
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import ListView, DetailView
from Loysen.blog.views import BlogView, BlogPostView, PostList
from Loysen.blog.models import Post


urlpatterns = patterns('blog.views',
    (r'^$',
        BlogView.as_view()),
    (r'^(?P<pk>\d+)/$',
        BlogPostView.as_view()),
    url(r'^api/$', 'api_root'),
    url(r'^api/posts/$', PostList.as_view(), name='post-list'),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

# Default login/logout views
urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)