from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    处理`Comment`模型上CRUD操作的视图集。
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """创建评论时，将当前已认证用户设为评论的作者"""
        if self.request.user and self.request.user.is_authenticated:
            serializer.save(user=self.request.user)

    def get_queryset(self):
        """
        根据认证用户（如适用）过滤评论。
        如果用户已认证且为管理员，则返回所有评论；
        否则，只返回该用户创建的评论。
        """
        queryset = super().get_queryset()
        if self.request.user and self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return queryset
            else:
                return queryset.filter(user=self.request.user)
        return queryset

    def perform_update(self, serializer):
        """
        防止修改`CommentSerializer`中定义为只读的`post`、`user`和`created_at`字段。
        """
        if 'post' in serializer.validated_data:
            del serializer.validated_data['post']
        if 'user' in serializer.validated_data:
            del serializer.validated_data['user']
        if 'created_at' in serializer.validated_data:
            del serializer.validated_data['created_at']
        serializer.save()

    def perform_destroy(self, instance):
        """
        只允许评论的作者或管理员删除评论，
        否则抛出`PermissionDenied`异常。
        """
        if self.request.user and self.request.user.is_authenticated:
            if self.request.user == instance.user or self.request.user.is_superuser:
                instance.delete()
            else:
                raise PermissionDenied("您无权删除此评论。")
        else:
            raise PermissionDenied("您必须登录后才能删除评论。")