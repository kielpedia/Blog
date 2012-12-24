'''
Created on Aug 10, 2011

@author: kiel
'''
from Loysen.blog.models import Post, Comment
from Loysen.blog.serializers import PostSerializer, CommentSerializer
from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'posts': reverse('post-list', request=request),
    })
    
class PostList(generics.ListAPIView):
    """
    API endpoint that represents a list of users.
    """
    model = Post
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a list of users.
    """
    model = Post
    serializer_class = PostSerializer

class PostCommentList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of users.
    """
    model = Comment
    serializer_class = CommentSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        post_id = self.kwargs['pk']
        return Comment.objects.filter(post=post_id)


class PostCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a list of users.
    """
    model = Comment
    serializer_class = CommentSerializer
    pk_url_kwarg = 'comment_id'



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