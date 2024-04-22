from rest_framework import mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import CartSerializer
from .models import Cart
from common.permission import CartPermission

class CartView(GenericViewSet, mixins.CreateModelMixin, 
                mixins.ListModelMixin, mixins.DestroyModelMixin, 
                mixins.UpdateModelMixin):
        
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, CartPermission]

    def get_serializer_class(self):
        return self.serializer_class
    
    def create(self, request, *args, **kwargs):
        user = request.user
        course = request.data.get('course')
        request.data['user'] = user.id
        return super().create(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = self.get_queryset().filter(user=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        user = request.user
        course = request.data.get('course')
        cart = self.get_queryset().filter(user=user, courses=course)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)