from rest_framework import serializers
from .models import Coupon

class CouponSerializer(serializers.Serializer):

    class Meta:
        model = Coupon
        fields = ('id', 'name', 'type', 'money', 'user', 'condition', 'per_limit')

class CouponReadSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display')
    class Meta:
        model = Coupon
        fields = ('id', 'name', 'type', 'money', 'user', 'condition', 'per_limit')
