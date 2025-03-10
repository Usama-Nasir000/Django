from django.db import models
from api.models.user_model import CustomUser
from api.models.campaign_model import Campaign

class Post(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="posts")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="posts")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user.username} in {self.campaign.title}"
