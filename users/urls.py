from django.urls import path
from users.views import RegistrationAPIView, AuthorizationAPIView, ConfirmUserAPIView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from users.views import CustomTokenObtainPairView
from users.oauth import GoogleAPIView
urlpatterns = [
    path("registration/", RegistrationAPIView.as_view()),
    path("authorization/", AuthorizationAPIView.as_view()),
    path("confirm/", ConfirmUserAPIView.as_view()),
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("google-login/", GoogleAPIView.as_view(), name="google_login"),
]
