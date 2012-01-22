'''
Created on Aug 13, 2011

@author: kiel
'''
from django.conf.urls.defaults import patterns
from django.views.generic import ListView, DetailView
from Loysen.blog.models import Post


urlpatterns = patterns('blog.views',
    (r'^$',
        ListView.as_view(
            queryset = Post.objects.order_by('-pub_date')[:5],
            context_object_name = 'latest_post_list',
            template_name = 'blog/index.html'
            )),
    (r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model = Post,
            template_name = 'blog/detail.html')),
)
