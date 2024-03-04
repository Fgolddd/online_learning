from django.db import models

# Create your models here.

class Banner(models.Model):
    title = models.CharField(max_length=255, verbose_name="标题")
    line = models.CharField(max_length=255, verbose_name="链接")
    image_url = models.CharField(max_length=255, verbose_name="图片")
    remark = models.TextField(verbose_name="备注信息")
    is_show = models.BooleanField(default=False, verbose_name="是否显示")
    priority = models.IntegerField(default=1, verbose_name="排序优先级")
    is_deleted = models.BooleanField(default=False, verbose_name="是否删除")

    class Meta:
        db_table = "home_banner"
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name
    
    # def __str__(self):
    #     return self.title