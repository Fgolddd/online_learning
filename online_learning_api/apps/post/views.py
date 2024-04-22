from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post
from .serializers import PostSerializer
from apps.comment.models import Comment
from apps.comment.serializers import CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    处理`Post`模型上CRUD操作的视图集。
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """创建帖子时，将当前已认证用户设为帖子的作者"""
        if self.request.user and self.request.user.is_authenticated:
            serializer.save(author=self.request.user)

    def get_queryset(self):
        """
        根据认证用户（如适用）过滤帖子。
        如果用户已认证且为管理员，则返回所有帖子；
        否则，只返回该用户创建的帖子。
        """
        queryset = super().get_queryset()
        if self.request.user and self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return queryset
            else:
                return queryset.filter(author=self.request.user)
        return queryset

    def perform_update(self, serializer):
        """
        防止修改`PostSerializer`中定义为只读的`created_at`和`updated_at`字段。
        """
        if 'created_at' in serializer.validated_data:
            del serializer.validated_data['created_at']
        if 'updated_at' in serializer.validated_data:
            del serializer.validated_data['updated_at']
        serializer.save()

    def perform_destroy(self, instance):
        """
        只允许帖子的作者或管理员删除帖子，
        否则抛出`PermissionDenied`异常。
        """
        if self.request.user and self.request.user.is_authenticated:
            if self.request.user == instance.author or self.request.user.is_superuser:
                instance.delete()
                # 删除与该帖子关联的所有评论
                Comment.objects.filter(post=instance).delete()
            else:
                raise PermissionDenied("您无权删除此帖子。")
        else:
            raise PermissionDenied("您必须登录后才能删除帖子。")