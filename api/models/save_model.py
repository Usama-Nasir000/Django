from django.db import models
from api.models.user_model import CustomUser
from api.models.post_model import Post
from api.models.campaign_model import Campaign

class Save(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="saves")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="saves", null=True, blank=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="saves", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'post', 'campaign')
    
    def __str__(self):
        return f"Save by {self.user.email}" 