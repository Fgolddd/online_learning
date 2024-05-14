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
    UserInfoViewSet,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    # 用户个人资料详情
    path('info/', UserInfoViewSet.as_view({
        'get': 'list',
    })),
    path('info/<int:pk>/', UserInfoViewSet.as_view({
        'get': 'retrieve',
        'put': 'partial_update',
    })),
    path('info/<int:pk>/change-password/', UserInfoViewSet.as_view({
        'put': 'change_password',
    })),
    path('info/<int:pk>/update-avatar/', UserInfoViewSet.as_view({
        'put': 'update_avatar',
    })),
    path('mycourse/', UserInfoViewSet.as_view({
        'get': 'my_course',
    }))

]   