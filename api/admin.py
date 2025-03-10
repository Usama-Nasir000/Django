from django.contrib import admin
from api.models.user_model import CustomUser
from api.models.campaign_model import Campaign, CampaignImage
from api.models.post_model import Post

admin.site.register(CustomUser)
admin.site.register(Campaign)
admin.site.register(CampaignImage)
admin.site.register(Post)