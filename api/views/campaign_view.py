from rest_framework import generics
from api.models.campaign_model import Campaign, CampaignImage
from api.serializers.campaign_serializer import CampaignSerializer, CampaignImageSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

# List all campaigns or create a new one
class CampaignListCreateView(generics.ListCreateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [IsAuthenticated]

# Retrieve, update, or delete a campaign
class CampaignDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [IsAuthenticated]

# Upload images separately (if needed)
class CampaignImageUploadView(generics.CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = CampaignImageSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        campaign_id = request.data.get("id")
        print(campaign_id)
        images = request.FILES.getlist("image")  # Multiple images

        try:
            campaign = Campaign.objects.get(id=campaign_id)
            for img in images:
                campaign.images.create(image=img)
                print(campaign) 
                # Assuming images field is related
            return Response({"message": "Images uploaded successfully"}, status=status.HTTP_201_CREATED)
        except Campaign.DoesNotExist:
            return Response({"error": "Campaign not found"}, status=status.HTTP_404_NOT_FOUND)
