import re
from rest_framework import status, mixins, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView
from common.permission import UserPermission
from .models import User
from .serializers import UserSerializer
# Create your views here.


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, UserPermission]


    @action(detail=False, methods=['put'], url_path='change-password')
    def change_password(self, request):
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')

        if not old_password or not new_password:
            return Response({'error': 'Both old and new passwords are required.'}, status=400)

        if not user.check_password(old_password):
            return Response({'error': 'Invalid old password.'}, status=400)

        user.set_password(new_password)
        user.save()

        return Response({'success': 'Password changed successfully.'})

    @action(detail=False, methods=['put'], url_path='update-avatar')
    def update_avatar(self, request):
        user = request.user
        serializer = self.serializer_class(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'success': 'Avatar updated successfully.'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['get'], url_path='avatar', url_name='retrieve_avatar')
    def retrieve_avatar(self, request):
        user = request.user

        if user.avatar:
            # 构建头像URL：MEDIA_URL + 'avatars/' + avatar_file_name
            avatar_url = f"{settings.MEDIA_URL}avatars/{user.avatar.name}"
            return Response({'avatar_url': avatar_url}, status=status.HTTP_200_OK)
        else:
            # 用户没有设置头像，返回相应提示
            return Response({'message': 'No avatar found for the user.'}, status=status.HTTP_404_NOT_FOUND)
class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        phone = request.data.get('phone')
        if not all([username, password, phone]):
            return Response({'error': '参数不能为空'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        if User.objects.filter(username=username).exists():
            return Response({'error': '用户名已存在'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        if User.objects.filter(phone=phone).exists():
            return Response({'error': '手机号已注册'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
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
        # result['avatar'] = serializer.user.avatar
        # result['collections'] = serializer.user.collections
        result['token'] = result.pop('access')

        return Response(result, status=status.HTTP_200_OK)