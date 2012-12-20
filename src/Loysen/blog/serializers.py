from Loysen.blog.models import Post
from rest_framework import serializers

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('subject', 'article', 'pub_date')