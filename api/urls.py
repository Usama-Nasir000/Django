from django.urls import path
from api.views import auth_view
from api.views.campaign_view import CampaignListCreateView, CampaignDetailView, CampaignImageUploadView
from api.views.post_view import PostListCreateView, PostDetailView


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('auth/register', auth_view.UserRegisterView.as_view(), name='register'),
    path('auth/login', auth_view.UserLoginView.as_view(), name='login'),
    
     path("campaigns/", CampaignListCreateView.as_view(), name="campaign-list-create"),
    path("campaigns/<int:pk>/", CampaignDetailView.as_view(), name="campaign-detail"),
    path("campaigns/images/upload/", CampaignImageUploadView.as_view(), name="campaign-image-upload"),

    # Post Endpoints
    path("posts/", PostListCreateView.as_view(), name="post-list-create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]
