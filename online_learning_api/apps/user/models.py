from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.course.models import Course
# Create your models here.

class User(AbstractUser):
    phone = models.CharField(verbose_name='手机号', max_length=11, unique=True)
    avatar = models.ImageField(verbose_name='用户头像',upload_to='avatars/', blank=True, null=True)
    collections = models.ManyToManyField(Course, verbose_name='收藏课程', blank=True)
    class Meta:
        db_table = 'onlearn_user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name