from rest_framework import generics
from api.models.post_model import Post
from api.serializers.post_serializer import PostSerializer

# Create & List Posts
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Retrieve a single post
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
