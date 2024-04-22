from rest_framework import viewsets, permissions
from .models import CourseCategory, Course
from .serializers import CourseCategorySerializer, CourseSerializer


# class CourseCategoryViewSet(viewsets.ModelViewSet):
#     queryset = CourseCategory.objects.all()
#     serializer_class = CourseCategorySerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(created_by=self.request.user)  # 如果需要记录创建者，可以在此处添加

#     def perform_update(self, serializer):
#         serializer.save(updated_by=self.request.user)  # 如果需要记录更新者，可以在此处添加


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


