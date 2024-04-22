from rest_framework import permissions

class UserPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        
        return obj == request.user



class CartPermission(permissions.BasePermission):
    """购物车对象操作权限"""

    def has_object_permission(self, request, view, obj):
        #判断操作的用户对象和登录的用户对象是否未同一个用户
        return obj.user == request.user

class OrderPermission(permissions.BasePermission):
    """订单对象操作权限"""

    def has_object_permission(self, request, view, obj):
        # 判断订单所属用户对象和登录的用户是否未同一个用户
        return obj.user == request.user


class CommentPermission(permissions.BasePermission):
    """订单对象操作权限"""

    def has_object_permission(self, request, view, obj):
        # 判断订单所属用户对象和登录的用户是否未同一个用户
        return obj.user == request.user