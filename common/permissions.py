from rest_framework import permissions
from rest_framework_jwt.authentication import jwt_decode_handler

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    视图级权限仅允许 admin 对其进行访问
    """
    def has_permission(self, request, view):
        print(request)
        print(view)
        print(request.user.username)
        if request.user.username=="admin":
            return True

    """
    对象级权限仅允许对象的所有者对其进行编辑
    假设模型实例具有`owner`属性。
    """

    def has_object_permission(self, request, view, obj):
        # 任何请求都允许读取权限，
        # 所以我们总是允许GET，HEAD或OPTIONS 请求.
        # if request.method in permissions.SAFE_METHODS:
        #     return True

        # return obj.user == request.user
        
        """
        对象级权限仅允许对象的所有者对其进行访问
        """

        token = request.META['HTTP_AUTHORIZATION'][5:]
        token_user = jwt_decode_handler(token) # 解码token
        print(token_user)
        print(obj.user.id)
        if token_user:
            return obj.user.id == token_user['user_id'] # 如果相同则返回True
        return False