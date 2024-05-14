from django.contrib import admin
from .models import Course, CourseCategory, Chapter, Video, SelledCourse
# Register your models here.

admin.site.register(Course)
admin.site.register(CourseCategory)
admin.site.register(Chapter)
admin.site.register(Video)
admin.site.register(SelledCourse)

