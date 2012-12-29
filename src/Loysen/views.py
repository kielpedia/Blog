'''
Created on Aug 10, 2011

@author: kiel
'''
from django.shortcuts import render_to_response
from django.template import RequestContext
from Loysen.blog.models import Post

def index(request):
    latestPosts = Post.objects.order_by('-pub_date')[:5]
    return render_to_response('index.html', {'latest_post_list': latestPosts}, context_instance=RequestContext(request))
