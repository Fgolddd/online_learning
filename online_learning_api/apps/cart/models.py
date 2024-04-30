from django.db import models
from apps.user.models import User
from apps.course.models import Course
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  verbose_name='用户')
    course =models.ForeignKey(Course, on_delete=models.CASCADE , verbose_name='课程')
    number = models.IntegerField(verbose_name='数量', default=1, blank=True, null=True)
    class Meta:
        db_table = 'onlearn_cart'
        verbose_name = '购物车'
        verbose_name_plural = verbose_name 
    def __str__(self):
        return self.user.username + '的购物车'