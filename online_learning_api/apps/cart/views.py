from rest_framework import mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import CartSerializer, CartReadSerializer
from .models import Cart
from common.permission import CartPermission

class CartView(GenericViewSet, mixins.CreateModelMixin, 
                mixins.ListModelMixin, mixins.DestroyModelMixin, 
                mixins.UpdateModelMixin):
        
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, CartPermission]

    def get_serializer_class(self):
        if self.action == 'list':
            return CartReadSerializer
        return self.serializer_class
    
    def create(self, request, *args, **kwargs):
        user = request.user
        course = request.data.get('course')

        if Cart.objects.filter(user=user, course=course).exists():
            cart_course = Cart.objects.get(user=user, course=course)
            cart_course.number += 1
            cart_course.save()
            
            serializer = self.get_serializer(cart_course)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            request.data['user'] = user.id
            return super().create(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = self.get_queryset().filter(user=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def update_course_number(self, request, *args, **kwargs):
        number = request.data.get('number')
        obj = self.get_object()

        if not isinstance(number, int):
            return Response({'error': '参数只能是数字，且不能为空'},
                            status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if number <= 0:
            obj.delete()
            return Response({'message': "修改成功,数量小于1，已经从购物车移除该商品"},
                            status=status.HTTP_200_OK)    
        else:
            obj.number = number
            obj.save()
            return Response({'message': "修改成功"},
                            status=status.HTTP_200_OK)