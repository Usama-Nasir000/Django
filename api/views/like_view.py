from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.models.post_model import Post
from api.serializers.post_serializer import PostSerializer
from api.models.campaign_model import Campaign
from api.serializers.campaign_serializer import CampaignSerializer
from api.serializers.like_save_comment_reply_serializer import LikeSerializer
from api.models.like_model import Like
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView



class LikeListCreateView(generics.ListCreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Like.objects.all()
        post_id = self.request.query_params.get("post_id")
        campaign_id = self.request.query_params.get("campaign_id")

        if post_id:
            queryset = queryset.filter(post_id=post_id)
        if campaign_id:
            queryset = queryset.filter(campaign_id=campaign_id)

        return queryset


class LikeDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        post_id = request.query_params.get("post_id")
        campaign_id = request.query_params.get("campaign_id")
        
        if not post_id and not campaign_id:
            return Response({"error": "Post ID or Campaign ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        like = Like.objects.filter(user=request.user, post_id=post_id, campaign_id=campaign_id).first()
        
        if like:
            like.delete()
            return Response({"message": "Like removed successfully"}, status=status.HTTP_204_NO_CONTENT)
        
        return Response({"error": "Like not found"}, status=status.HTTP_404_NOT_FOUND)
    
class UserLikedPostsView(generics.ListAPIView):
    serializer_class = PostSerializer  
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        liked_post_ids = Like.objects.filter(user=self.request.user, post__isnull=False).values_list("post_id", flat=True)
        return Post.objects.filter(id__in=liked_post_ids)

    
class UserLikedCampaignsView(generics.ListAPIView):
    serializer_class = CampaignSerializer  
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        liked_campaign_ids = Like.objects.filter(user=self.request.user, campaign__isnull=False).values_list("campaign_id", flat=True)
        return Campaign.objects.filter(id__in=liked_campaign_ids)
