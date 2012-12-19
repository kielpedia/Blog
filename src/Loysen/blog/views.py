'''
Created on Aug 10, 2011

@author: kiel
'''
from Loysen.blog.models import Post
from django.views.generic import TemplateView

class BlogView(TemplateView):
    template_name = "blog/index.html"


    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['latest_post_list'] = Post.objects.order_by('-pub_date')[:5]
        return context
        
class BlogPostView(BlogView):
    template_name = 'blog/detail.html'


    def get_context_data(self, **kwargs):
        context = super(BlogPostView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.kwargs['pk'])
        return context