from rest_framework import serializers
from api.models.campaign_model import Campaign, CampaignImage

class CampaignImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    
    class Meta:
        model = CampaignImage
        fields = ["id", "image"]

class CampaignSerializer(serializers.ModelSerializer):
    images = CampaignImageSerializer(many=True, read_only=True)  # Nested Serializer for Images

    class Meta:
        model = Campaign
        fields = "__all__"  # Include all fields including images
