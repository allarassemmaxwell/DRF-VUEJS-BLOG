from rest_framework import serializers
from .models import *




class PostSerializer(serializers.ModelSerializer):
    # cat_name = serializers.CharField(source='category.title', read_only=True)
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'thumbnail',
            'excerpt',
            'content',
            'slug',
            'published',
            'author',
            'status'    
        ]