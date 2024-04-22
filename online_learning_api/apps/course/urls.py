from django.contrib import admin
from django.urls import path, re_path

from .views import  CourseViewSet, ChapterViewSet

urlpatterns = [
    
    # 课程增删改查URL
    path('', CourseViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', CourseViewSet.as_view({'get': 'retrieve', 'put': 'update',  'delete': 'destroy'})),

    path('chapter/', ChapterViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('chapter/<int:pk>/', ChapterViewSet.as_view({'get': 'retrieve', 'put': 'update',  'delete': 'destroy'})),
]