'''
Created on Aug 13, 2011

@author: kiel
'''
from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from Loysen.blog.views import BlogView, BlogPostView, PostList, PostDetail, PostCommentList, PostCommentDetail


urlpatterns = patterns('blog.views',
    (r'^$',
        BlogView.as_view()),
    (r'^(?P<pk>\d+)/$',
        BlogPostView.as_view()),
    url(r'^api/$', 'api_root'),
    url(r'^api/posts/$', PostList.as_view(), name='post-list'),
    url(r'^api/posts/(?P<pk>\d+)/$', PostDetail.as_view(), name='post-detail'),
    url(r'^api/posts/(?P<pk>\d+)/comments/$', PostCommentList.as_view(), name='comment-list'),
    url(r'^api/posts/(?P<pk>\d+)/comments/(?P<comment_id>\d+)/$', PostCommentDetail.as_view(), name='comment-detail'),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

# Default login/logout views
urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)