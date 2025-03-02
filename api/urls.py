from django.urls import path
from api.views import auth_view


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('auth/register', auth_view.RegisterUser.as_view(), name='register'),
]
