from rest_framework import serializers
from datetime import datetime, timedelta
from django.utils import timezone
from .models import Post  
from apps.comment.serializers import CommentReadSerializer
from apps.user.serializers import UserSerializer, LimitedUserSerializer


class PostSerializer(serializers.ModelSerializer):
    comments = CommentReadSerializer(many=True, read_only=True)
    created_at = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ('id', 'content', 'author', 'comments','created_at',)
    def get_created_at(self, obj):
        now = timezone.now()
        delta = now - obj.created_at

        if delta.days == 0 and delta.seconds < 3600:  # Within the last hour
            minutes = delta.seconds // 60
            return f"{minutes}分钟前"

        return obj.created_at.strftime("%H:%M %m-%d")

class PostReadSerializer(serializers.ModelSerializer):
    comments = CommentReadSerializer(many=True, read_only=True)
    author = LimitedUserSerializer(many=False, read_only=True)
    created_at = serializers.SerializerMethodField()
    # updated_at = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ('id', 'content', 'author', 'comments','created_at', 'thumbs_up')  # 根据您的 `Post` 模型字段调整

    def get_created_at(self, obj):
        now = timezone.now()
        delta = now - obj.created_at

        if delta.days == 0 and delta.seconds < 3600:  # Within the last hour
            minutes = delta.seconds // 60
            return f"{minutes}分钟前"

        return obj.created_at.strftime("%H:%M %m-%d")
    
    
    # def updated_at(self, obj):
    #     now = timezone.now()
    #     delta = now - obj.updated_at

    #     if delta.days == 0 and delta.seconds < 3600:  # Within the last hour
    #         minutes = delta.seconds // 60
    #         return f"{minutes}分钟前"

    #     return obj.updated_at.strftime("%Y-%m-%d")
    
