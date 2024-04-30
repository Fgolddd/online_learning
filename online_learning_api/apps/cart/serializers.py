from rest_framework import serializers

from .models import Cart
from apps.course.serializers import CartCourseSerializer

class CartReadSerializer(serializers.ModelSerializer):
    course = CartCourseSerializer()
    class Meta:
        model = Cart
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'    

         
