from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer, CommentReadSerializer
from common.permission import CommentPermission


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, CommentPermission]

    def get_serializer_class(self):
        if self.action == 'list':
            return CommentReadSerializer
        return CommentSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        request.data['user'] = user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = serializer.instance.user

        res = serializer.data.copy()
        res['user'] = {
            'id': user.id,
            'username': user.username,
            'avatar': user.avatar.url
        }
        return Response(res, status=status.HTTP_201_CREATED)

        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  # 获取要删除的Post对象
        self.perform_destroy(instance)  # 执行删除操作

        # 返回删除成功的响应
        return Response(
            {'message': '评论删除成功'},
            status=status.HTTP_204_NO_CONTENT
        )