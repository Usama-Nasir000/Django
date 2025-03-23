from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.serializers.like_save_comment_reply_serializer import ReplySerializer
from api.models.reply_model import Reply

class ReplyListCreateView(generics.ListCreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [IsAuthenticated]

class ReplyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [IsAuthenticated]