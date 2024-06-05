import datetime
import time
from django.db import transaction
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import viewsets
from apps.order.models import Order, OrderCourse
from apps.cart.models import Cart
from apps.order.serializers import OrderSerializer
from common.permission import OrderPermission

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, OrderPermission]

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

    def partial_update(self, request, *args, **kwargs):
        """
        更新订单的支付状态。
        """
        ORDER_STATUS = (
        (1, '待支付'),
        (2, '已支付'),
        )
        instance = self.get_object()  # 获取需要更新的订单实例
        new_status = request.data.get('status')  # 假设前端发送的是 {'status': 2} 来表示已支付状态
        
        # 验证新状态是否有效
        valid_statuses = {status[0] for status in ORDER_STATUS}
        if new_status not in valid_statuses:
            return Response({"error": "无效的订单状态"}, status=status.HTTP_400_BAD_REQUEST)
        
        # 更新订单状态
        instance.status = new_status
        instance.save(update_fields=['status'])  # 只更新指定字段

        serializer = self.get_serializer(instance)  # 序列化更新后的对象
        return Response(serializer.data)