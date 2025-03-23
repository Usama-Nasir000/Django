from rest_framework import serializers
from api.models.reply_model import Reply
from api.models.save_model import Save
from api.models.campaign_model import Campaign
from api.models.like_model import Like
from api.models.comment_model import Comment

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class SaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Save
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'