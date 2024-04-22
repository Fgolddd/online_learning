from django.contrib import admin
from django.urls import path

from .views import PostViewSet

urlpatterns = [
    path('', PostViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),

    path('<int:pk>/', PostViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        
        'delete': 'destroy'
    })),
]