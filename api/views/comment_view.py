from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.serializers.like_save_comment_reply_serializer import CommentSerializer
from api.models.comment_model import Comment

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]