from django.db import models
from apps.user.models import User
from apps.post.models import Post
class Comment(models.Model):
    """
    帖子评论模型
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='所属帖子', blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forum_comments', verbose_name='评论者', blank=False, null=False)
    content = models.TextField(verbose_name='评论内容')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return f'{self.user.username} 在 {self.post.author} 的帖子 {self.post.pk} 的评论'

    class Meta:
        db_table = 'onlearn_comment'
        ordering = ['-created_at']
        verbose_name = '评论'
        verbose_name_plural = verbose_name