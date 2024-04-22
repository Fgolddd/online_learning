from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from apps.comment.models import Comment
from apps.comment.serializers import CommentSerializer
from common.permission import PostPermission


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PostPermission]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  # 获取要删除的Post对象
        self.perform_destroy(instance)  # 执行删除操作

        # 返回删除成功的响应
        return Response(
            {'message': '帖子删除成功'},
            status=status.HTTP_204_NO_CONTENT
        )