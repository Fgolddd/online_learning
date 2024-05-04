from datetime import datetime, timedelta
from django.utils import timezone

from rest_framework import serializers
from apps.course.serializers import CartCourseSerializer
from apps.order.models import Order, OrderCourse

class OrderCourseSerializer(serializers.ModelSerializer):
    course = CartCourseSerializer()

    class Meta:
        model = OrderCourse
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    order_goods_set = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'order_code', 'amount', 'created_at', 'order_goods_set')

    def get_order_goods_set(self, obj):
        order_goods_set = OrderCourse.objects.filter(order=obj)
        return OrderCourseSerializer(order_goods_set, many=True).data

    def get_created_at(self, obj):
        
        return obj.created_at.strftime("%m-%d %H:%M")