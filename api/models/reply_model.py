from django.db import models
from api.models.user_model import CustomUser
from api.models.comment_model import Comment

class Reply(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="replies")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Reply by {self.user.email}" 