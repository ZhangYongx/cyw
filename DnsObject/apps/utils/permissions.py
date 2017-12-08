# -*- coding: utf-8 -*-
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    对象级权限只允许对象的所有者修改、删除。
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.create_user == request.user.username
