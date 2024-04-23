from rest_framework import serializers
from .models import User
from apps.course.serializers import CollectionCourseSerializer

class UserSerializer(serializers.ModelSerializer):
    collections = CollectionCourseSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'phone',
            'avatar',
            'password',
            'is_staff', 
            'collections',
        )
        


    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        return super().update(instance, validated_data)

class UserCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)