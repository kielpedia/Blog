from Loysen.blog.models import Post, Comment
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.ManyHyperlinkedRelatedField(source='comment_set', view_name='comment-list', read_only=True)

    class Meta:
        model = Post
        read_only_fields = ('subject', 'pub_date')

class CommentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Comment
        exclude = {'subject',}
        read_only_fields = {'pub_date'}
