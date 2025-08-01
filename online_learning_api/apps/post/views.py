from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer, PostReadSerializer
from apps.comment.models import Comment
from apps.comment.serializers import CommentSerializer
from common.permission import PostPermission
from rest_framework.decorators import action

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PostPermission]

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return PostReadSerializer
        return PostSerializer

    def create(self, request, *args, **kwargs):
        author = request.user
        request.data['author'] = author.id
        return super().create(request, *args, **kwargs)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  # 获取要删除的Post对象
        self.perform_destroy(instance)  # 执行删除操作

        # 返回删除成功的响应
        return Response(
            {'message': '帖子删除成功'},
            status=status.HTTP_204_NO_CONTENT
        )

    @action(detail=False, methods=['put'], url_path='<int:pk>/thumbs_up')
    def handle_thumbs_up(self, request, *args, **kwargs):
        post = self.get_object()
        post.thumbs_up += 1
        post.save()
        return Response({'message': '点赞成功'}, status=status.HTTP_200_OK)