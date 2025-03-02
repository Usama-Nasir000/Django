from django.urls import path
from api.views import auth_view


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('auth/register', auth_view.UserRegisterView.as_view(), name='register'),
    path('auth/login', auth_view.UserLoginView.as_view(), name='login'),
    
]
