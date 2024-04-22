from rest_framework import serializers

from .models import Cart
from apps.course.serializers import CartCourseSerializer

class CartSerializer(serializers.ModelSerializer):
    courses = CartCourseSerializer(many=True, read_only=True) 

    class Meta:
        model = Cart
        fields = ('user', 'courses', )
    

         
