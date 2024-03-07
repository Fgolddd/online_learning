import re
from rest_framework import status, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
# Create your views here.


class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        phone = request.data.get('phone')
        password_confirmation = request.data.get('password_confirmation')
        if not all([username, password, phone, password_confirmation]):
            return Response({'error': '参数不能为空'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        if User.objects.filter(username=username).exists():
            return Response({'error': '用户名已存在'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        if User.objects.filter(phone=phone).exists():
            return Response({'error': '手机号已注册'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        if password != password_confirmation:
            return Response({'error': '密码不一致'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if not (6 <= len(password) <= 18):
            return Response({'error': '密码长度要在6-18位'}, status=status.HTTP_400_BAD_REQUEST)

        if not re.match(r'^1[3456789]\d{9}$', phone):
            return Response({'error': '手机号码格式错误'}, status=status.HTTP_400_BAD_REQUEST)
        
        obj = User.objects.create_user(
            username=username, 
            phone=phone, 
            password=password
        )

        res = {
            'username': username,
            'id': obj.id,
            'phone': obj.phone
        }
        return Response(res, status=status.HTTP_201_CREATED)

class LoginView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        
        result = serializer.validated_data
        result['id'] = serializer.user.id
        result['phone'] = serializer.user.phone
        result['username'] = serializer.user.username
        result['token'] = result.pop('access')

        return Response(result, status=status.HTTP_200_OK)