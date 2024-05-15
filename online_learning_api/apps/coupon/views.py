from rest_framework import viewsets, permissions
from .models import Coupon
from .serializers import CouponReadSerializer
# Create your views here.

class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponReadSerializer
    permission_classes = [permissions.IsAuthenticated]