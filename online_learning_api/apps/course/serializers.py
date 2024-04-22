from rest_framework import serializers
from .models import CourseCategory, Course

class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ('id', 'name', 'remark')
        read_only_fields = ('id',)


class CourseSerializer(serializers.ModelSerializer):
    category = CourseCategorySerializer(read_only=True)

    class Meta:
        model = Course
        fields = (
            'id', 'name', 'course_cover', 'course_video', 'course_type',
            'description', 'status','students', 'price', 'chapters', 
            'category','attachment_path', 'attachment_link',
        )
        read_only_fields = ('id', 'students')

class CollectionCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'price', 'course_cover')