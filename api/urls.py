from django.urls import path
from api.views.comment_view import CommentDetailView, CommentListCreateView
from api.views.like_view import LikeDeleteView, LikeListCreateView, UserLikedCampaignsView, UserLikedPostsView
from api.views.reply_view import ReplyDetailView, ReplyListCreateView
from api.views.save_view import SaveDeleteView, SaveListCreateView, UserSavedCampaignsView, UserSavedPostsView
from api.views import auth_view
from api.views.campaign_view import CampaignListCreateView, CampaignDetailView, CampaignImageUploadView
from api.views.post_view import PostListCreateView, PostDetailView


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('auth/register', auth_view.UserRegisterView.as_view(), name='register'),
    path('auth/login', auth_view.UserLoginView.as_view(), name='login'),
    path('auth/logout', auth_view.UserLogoutView.as_view(), name='logout'),
    
    # Campaign Endpoints
    path("campaigns/", CampaignListCreateView.as_view(), name="campaign-list-create"),
    path("campaigns/<int:pk>/", CampaignDetailView.as_view(), name="campaign-detail"),
    path("campaigns/images/upload/", CampaignImageUploadView.as_view(), name="campaign-image-upload"),

    # Post Endpoints
    path("posts/", PostListCreateView.as_view(), name="post-list-create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    
    #Like Endpoints
    path("likes/", LikeListCreateView.as_view(), name="like-list-create"),
    path("likes/remove/", LikeDeleteView.as_view(), name="like-remove"),
    
    #Save Endpoints
    path("saves/", SaveListCreateView.as_view(), name="save-list-create"),
    path("saves/remove/", SaveDeleteView.as_view(), name="save-remove"),
    
    #Comment Endpoint
    path("comments/", CommentListCreateView.as_view(), name="comment-list-create"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comment-detail"),
    
    #Reply Endpoint
    path("replies/", ReplyListCreateView.as_view(), name="reply-list-create"),
    path("replies/<int:pk>/",ReplyDetailView.as_view(), name="reply-detail"),
]

urlpatterns += [
    path("likes/user/posts/", UserLikedPostsView.as_view(), name="user-liked-posts"),
    path("likes/user/campaigns/", UserLikedCampaignsView.as_view(), name="user-liked-campaigns"),
]

urlpatterns += [
    path("saves/user/posts/", UserSavedPostsView.as_view(), name="user-saved-posts"),
    path("saves/user/campaigns/", UserSavedCampaignsView.as_view(), name="user-saved-campaigns"),
]
