from rest_framework import serializers
from .models import CourseCategory, Course, Chapter, Video, SelledCourse

class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ('id', 'name', 'remark')

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'link')


class ChapterSerializer(serializers.ModelSerializer):
    video = VideoSerializer(many=True, read_only=True)
    class Meta:
        model = Chapter
        fields = ('id', 'title', 'video')

class CourseSerializer(serializers.ModelSerializer):
    category = CourseCategorySerializer(read_only=True)
    chapters = ChapterSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = (
            'id', 'name', 'course_cover',  'course_type',
            'description','chapters', 'status','students', 'price', 
            'category', 'attachment_link',
        )
        
class CartCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'course_cover', 'price', 'students')

class SelledCourseSerializer(serializers.ModelSerializer):
    course = CartCourseSerializer()
    class Meta:
        model = SelledCourse
        fields = ('id', 'course', 'user')

