from django.apps import AppConfig


class CommentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.comment'
    # verbose_name = '评论管理'
    # verbose_name_plural = verbose_name