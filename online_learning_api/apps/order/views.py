import datetime
import time
from django.db import transaction
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from apps.order.models import Order, OrderCourse
from apps.cart.models import Cart
from apps.order.serializers import OrderSerializer
# from common.permission import CartPermission

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(user=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        
    def create(self, request, *args, **kwargs):
        order_code = str(int(time.time())) + str(request.user.id)
        cart_course = Cart.objects.filter(user=request.user)
       
        # save_id = transaction.savepoint()
        
        if not cart_course.exists():
            return Response({'error': "订单创建失败，未选中商品"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        try:
            order = Order.objects.create(user=request.user,order_code=order_code,amount=0)
            
            amount = 0
            for cart in cart_course:
                amount += cart.course.price * cart.number
                OrderCourse.objects.create(order=order, course=cart.course,
                                            price=cart.course.price, number=cart.number)
                                          
                cart.delete()
            
            order.amount = amount
            order.save()
            
            # transaction.savepoint_commit(save_id)
            serializer = self.get_serializer(order)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            # transaction.savepoint_rollback(save_id)
            return Response({'error': "服务处理异常，订单创建失败！"}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
