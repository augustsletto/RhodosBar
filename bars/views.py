from rest_framework import viewsets
from .models import Bar, Post
from .serializers import BarSerializer, PostSerializer

class BarViewSet(viewsets.ModelViewSet):
    queryset = Bar.objects.all()
    serializer_class = BarSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
