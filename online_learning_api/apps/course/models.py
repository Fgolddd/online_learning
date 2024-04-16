from django.db import models
from common.base_model import BaseModel
from django_ckeditor_5.fields import CKEditor5Field
from stdimage import StdImageField
# Create your models here.
class CourseCategory(BaseModel):
    name = models.CharField(max_length=255, unique=True, verbose_name="分类名称")
    remark = CKEditor5Field(max_length=255, default="", blank=True, null=True, verbose_name="分类描述")
    
    class Meta:
        db_table = "onlearn_course_category"
        verbose_name = "课程分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Course(BaseModel):
    course_type = ((0, "免费课程"), (1, "付费课程"))
    status = ((0, "下线"), (1, "上线"))

    course_cover = StdImageField(variations={
        'thumb_1080x608': (1080, 608),  # 高清图
        'thumb_540x304': (540, 304),  # 中等比例,
        'thumb_108x61': (108, 61, True),  # 小图(第三个参数表示保持图片质量),
    }, max_length=255, delete_orphans=True, upload_to="course/cover", null=True,
    verbose_name="封面图片", blank=True)
    course_video = models.FileField(upload_to="course/video", max_length=255, blank=True, null=True,
                                    verbose_name="封面视频")
    
    course_type = models.SmallIntegerField(choices=course_type, default=0, verbose_name="付费类型")
    description = CKEditor5Field(blank=True, null=True, verbose_name="详情介绍")
    attachment_path = models.CharField(max_length=1000, blank=True, null=True, verbose_name="课件路径")
    attachment_link = models.CharField(max_length=1000, blank=True, null=True, verbose_name="课件链接")
    status = models.SmallIntegerField(choices=status, default=0, verbose_name="课程状态")
    students = models.IntegerField(default=0, verbose_name="学习人数")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="课程原价")
    category = models.ForeignKey("CourseCategory", related_name="course_list", on_delete=models.DO_NOTHING,
                                 db_constraint=False, null=True, blank=True, verbose_name="学习分类")
    class Meta:
        db_table = "onlearn_course_info"
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.name