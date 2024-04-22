from rest_framework import serializers
from datetime import datetime, timedelta
from django.utils import timezone
from .models import Post  
from apps.comment.serializers import CommentSerializer
from apps.users.serializers import UserSerializer

class LimitedUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ('id', 'username', 'avatar')


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    author = LimitedUserSerializer(many=False, read_only=True)
    created_at = serializers.SerializerMethodField()
    # updated_at = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ('id', 'content', 'author', 'comments','created_at')  # 根据您的 `Post` 模型字段调整

    # def validate_author(self, value):
    #     try:
    #         user = User.objects.get(pk=value)
    #     except User.DoesNotExist:
    #         raise serializers.ValidationError("指定的 author ID 对应的用户不存在。")
        
    #     if not user.is_active:  # 可选：检查用户是否处于活跃状态
    #         raise serializers.ValidationError("指定的 author ID 对应的用户已被禁用。")

    #     return user

    # def create(self, validated_data):
    #     post = Post.objects.create(**validated_data)  # 创建 Post 实例
    #     # 如果客户端在创建帖子时同时提交了评论数据（假设通过 `comments` 字段）
    #     if 'comments' in validated_data:
    #         comment_data_list = validated_data.pop('comments')  # 从 validated_data 中移除 comments 字段
    #         for comment_data in comment_data_list:
    #             comment = Comment.objects.create(post=post, **comment_data)  # 为新创建的 Post 创建关联的 Comment
    #     return post

    def get_created_at(self, obj):
        now = timezone.now()
        delta = now - obj.created_at

        if delta.days == 0 and delta.seconds < 3600:  # Within the last hour
            minutes = delta.seconds // 60
            return f"{minutes}分钟前"

        return obj.created_at.strftime("%m-%d %H:%M")
    
    
    # def updated_at(self, obj):
    #     now = timezone.now()
    #     delta = now - obj.updated_at

    #     if delta.days == 0 and delta.seconds < 3600:  # Within the last hour
    #         minutes = delta.seconds // 60
    #         return f"{minutes}分钟前"

    #     return obj.updated_at.strftime("%Y-%m-%d")
    
