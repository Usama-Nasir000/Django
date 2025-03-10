from django.db import models
from api.models.user_model import CustomUser

class Campaign(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("completed", "Completed"),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="campaigns")
    title = models.CharField(max_length=255)
    description = models.TextField()
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    raised_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class CampaignImage(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="campaign_images/")

    def __str__(self):
        return f"Image for {self.campaign.title}"
