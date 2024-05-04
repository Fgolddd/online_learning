from rest_framework import permissions

class UserPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        
        return obj == request.user

class CartPermission(permissions.BasePermission):
    """订单对象操作权限"""

    def has_object_permission(self, request, view, obj):
        # 判断购物车所属用户对象和登录的用户是否未同一个用户
        return obj.user == request.user

class OrderPermission(permissions.BasePermission):
    """订单对象操作权限"""

    def has_object_permission(self, request, view, obj):
        # 判断订单所属用户对象和登录的用户是否未同一个用户
        return obj.user == request.user

class PostPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if view.action in ['list']:
            # 对于PostList视图，无需登录即可访问
            return True

        # 对于PostCreate与PostDelete视图，需要用户登录
        return obj.author == request.user or request.user.is_superuser

class CommentPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if view.action in ['list']:
            # 对于PostList视图，无需登录即可访问
            return True

        # 对于PostCreate与PostDelete视图，需要用户登录
        return obj.user == request.user or request.user.is_superuser
        

