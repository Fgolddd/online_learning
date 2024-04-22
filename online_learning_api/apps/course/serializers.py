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

class CourseChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name',)

class CourseSerializer(serializers.ModelSerializer):
    category = CourseCategorySerializer(read_only=True)

    class Meta:
        model = Course
        fields = (
            'id', 'name', 'course_cover',  'course_type',
            'description', 'status','students', 'price', 
            'category','attachment_path', 'attachment_link',
        )
        read_only_fields = ('id', 'students')

class CollectionCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'price', 'course_cover')

class ChapterSerializer(serializers.ModelSerializer):
    course = CourseChapterSerializer(read_only=True)
    video = VideoSerializer(many=True, read_only=True)
    class Meta:
        model = Chapter
        fields = ('id','course', 'title', 'video')