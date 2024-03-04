from django.contrib import admin
from django.urls import path, re_path
from rest_framework_simplejwt.views import (
    TokenRefreshView, 
    TokenVerifyView, 
    TokenObtainPairView
)
from .views import (
    RegisterView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
    path('register/', RegisterView.as_view()),
]   