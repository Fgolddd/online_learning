from rest_framework import viewsets, permissions
from .models import Chapter, Course
from .serializers import  CourseSerializer, ChapterSerializer



class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
