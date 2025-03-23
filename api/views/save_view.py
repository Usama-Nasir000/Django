from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.models.campaign_model import Campaign
from api.models.post_model import Post
from api.serializers.campaign_serializer import CampaignSerializer
from api.serializers.post_serializer import PostSerializer
from api.serializers.like_save_comment_reply_serializer import SaveSerializer
from api.models.save_model import Save
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView



class SaveListCreateView(generics.ListCreateAPIView):
    serializer_class = SaveSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Save.objects.all()
        post_id = self.request.query_params.get("post_id")
        campaign_id = self.request.query_params.get("campaign_id")

        if post_id:
            queryset = queryset.filter(post_id=post_id)
        if campaign_id:
            queryset = queryset.filter(campaign_id=campaign_id)

        return queryset


class SaveDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        post_id = request.query_params.get("post_id")
        campaign_id = request.query_params.get("campaign_id")
        
        if not post_id and not campaign_id:
            return Response({"error": "Post ID or Campaign ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        save = Save.objects.filter(user=request.user, post_id=post_id, campaign_id=campaign_id).first()
        
        if save:
            save.delete()
            return Response({"message": "Save removed successfully"}, status=status.HTTP_204_NO_CONTENT)
        
        return Response({"error": "Save not found"}, status=status.HTTP_404_NOT_FOUND)



class UserSavedPostsView(generics.ListAPIView):
    serializer_class = PostSerializer  
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        saved_post_ids = Save.objects.filter(user=self.request.user, post__isnull=False).values_list("post_id", flat=True)
        return Post.objects.filter(id__in=saved_post_ids)

class UserSavedCampaignsView(generics.ListAPIView):
    serializer_class = CampaignSerializer  
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        saved_campaign_ids = Save.objects.filter(user=self.request.user, campaign__isnull=False).values_list("campaign_id", flat=True)
        return Campaign.objects.filter(id__in=saved_campaign_ids)
