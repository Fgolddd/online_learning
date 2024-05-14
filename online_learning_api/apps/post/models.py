# forum/models.py

from django.db import models
from apps.user.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from mdeditor.fields import MDTextField

class Post(models.Model):
    """
    论坛帖子模型
    """
    content = MDTextField(verbose_name='内容')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name='作者')
    thumbs_up = models.IntegerField(default=0, verbose_name='点赞数')
    
    tags = TaggableManager(blank=True, verbose_name='标签')

    def __str__(self):
        return self.author.username + '的帖子'

    class Meta:
        db_table = 'onlearn_post'
        ordering = ['-created_at']
        verbose_name = '帖子'
        verbose_name_plural = verbose_name


