from rest_framework import generics
from app.models import Post
from app.api.serializers import PostSerializer , PostDetailSerializer ,PostDeleteSerializer
from app.api.serializers import PostUpdateSerializer

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDitailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer    
    lookup_field = 'id'

class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDeleteSerializer    
    lookup_field = 'id'


class PostUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer    
    lookup_field = 'id'

