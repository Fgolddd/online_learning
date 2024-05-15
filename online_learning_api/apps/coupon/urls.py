from django.contrib import admin
from django.urls import path

from .views import CouponViewSet

urlpatterns = [
    path('', CouponViewSet.as_view( {
        'get': 'list',
        'post': 'create'
    })),
    path('<int:pk>/', CouponViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy'
    })),  
]