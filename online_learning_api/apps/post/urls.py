from django.contrib import admin
from django.urls import path

from .views import PostViewSet

urlpatterns = [
    path('', PostViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='comment-list'),

    path('<int:pk>/', PostViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='comment-detail'),
]