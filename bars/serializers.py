from rest_framework import serializers
from .models import Bar, Post

class BarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bar
        fields = ('id', 'owner', 'name', 'description', 'location', 'logo')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'bar', 'image', 'video', 'description', 'created_at')
