from rest_framework import serializers
from .models import CourseCategory, Course, Chapter, Video

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
            'category','attachment_path', 'attachment_link',
        )
        

class CollectionCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'price', 'course_cover')

