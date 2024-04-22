from rest_framework import serializers
from datetime import datetime, timedelta
from django.utils import timezone
from .models import Comment  
from apps.user.serializers import UserCommentSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserCommentSerializer(read_only=True)
    created_at = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ('id', 'post', 'user', 'content', 'created_at')  # 包含所有字段

    def get_created_at(self, obj):
        now = timezone.now()
        delta = now - obj.created_at

        if delta.days == 0 and delta.seconds < 3600:  # Within the last hour
            minutes = delta.seconds // 60
            return f"{minutes}分钟前"

        return obj.created_at.strftime("%m-%d %H:%M")