from rest_framework import serializers
from datetime import datetime, timedelta
from django.utils import timezone
from .models import Comment  

class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ('id', 'post', 'user', 'content', 'created_at')  # 包含所有字段
        read_only_fields = ('post', 'user', 'created_at')  # 这些字段通常由系统自动管理，客户端不应直接修改

    def get_created_at(self, obj):
        now = timezone.now()
        delta = now - obj.created_at

        if delta.days == 0 and delta.seconds < 3600:  # Within the last hour
            minutes = delta.seconds // 60
            return f"{minutes}分钟前"

        return obj.created_at.strftime("%m-%d %H:%M")