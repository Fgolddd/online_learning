from django.db import models
from common.base_model import BaseModel
from mdeditor.fields import MDTextField

# Create your models here.
class CourseCategory(BaseModel):
    name = models.CharField(max_length=255, unique=True, verbose_name="分类名称")
    remark = models.TextField(
        max_length=255,
        default="",
        blank=True,
        null=True,
        verbose_name="分类描述"
    )    
    class Meta:
        db_table = "onlearn_course_category"
        verbose_name = "课程分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Chapter(models.Model):
    course = models.ForeignKey("Course", on_delete=models.DO_NOTHING,related_name="chapters",
                                 db_constraint=False, null=True, blank=True, verbose_name="课程章节")
    title = models.CharField(max_length=255, verbose_name="章节标题")
    video = models.ManyToManyField("Video", verbose_name="视频", blank=True)
    
    class Meta:
        db_table = "onlearn_course_chapter"
        verbose_name = "课程章节"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return "%s" % self.title

class Video(models.Model):
    title = models.CharField(max_length=255, verbose_name="视频标题")
    link = models.URLField(max_length=255, verbose_name="视频链接")

    class Meta:
        db_table = "onlearn_course_video"
        verbose_name = "课程视频"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return "%s" % self.title

class Course(BaseModel):
    course_type = ((0, "免费课程"), (1, "付费课程"))
    status = ((0, "下线"), (1, "上线"))
    course_cover = models.ImageField(max_length=255, upload_to="course/cover/", null=True,
    verbose_name="封面图片", blank=True)
    course_type = models.SmallIntegerField(choices=course_type, default=0, verbose_name="付费类型")
    description = MDTextField(blank=True, null=True, verbose_name="详情介绍")
    attachment_link = models.URLField(max_length=1000, blank=True, null=True, verbose_name="课件链接")
    status = models.SmallIntegerField(choices=status, default=0, verbose_name="课程状态")
    students = models.IntegerField(default=0, verbose_name="学习人数")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="课程原价")
    category = models.ForeignKey("CourseCategory", related_name="course_list", on_delete=models.DO_NOTHING,
                                 db_constraint=False, null=True, blank=True, verbose_name="课程分类")

    class Meta:
        db_table = "onlearn_course_info"
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.name

class SelledCourse(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.DO_NOTHING,
                             db_constraint=False, null=True, blank=True, verbose_name="用户")
    course = models.ForeignKey("Course", on_delete=models.DO_NOTHING,
                               db_constraint=False, null=True, blank=True, verbose_name="课程")

    class Meta:
        db_table = "onlearn_selled_course"
        verbose_name = "已购课程"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return "%s" % self.user