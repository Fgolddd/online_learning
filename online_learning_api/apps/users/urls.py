from django.contrib import admin
from django.urls import path, re_path
from rest_framework_simplejwt.views import (
    TokenRefreshView, 
    TokenVerifyView, 
    TokenObtainPairView
)
from .views import (
    RegisterView,
    LoginView,
    UserProfileViewSet
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    # 用户个人资料详情
    path('profiles/', UserProfileViewSet.as_view({
        'get': 'list',
    }), name='profile-list'),
    path('profiles/<int:pk>/', UserProfileViewSet.as_view({
        'get': 'retrieve',
        'put': 'partial_update',
    }), name='profile-detail'),
    path('profiles/<int:pk>/change-password/', UserProfileViewSet.as_view({
        'put': 'change_password',
    }), name='profile-change-password'),
    path('profiles/<int:pk>/update-avatar/', UserProfileViewSet.as_view({
        'put': 'update_avatar',
    }), name='profile-update-avatar'),
]   