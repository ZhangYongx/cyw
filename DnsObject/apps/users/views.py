# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from users import models
from rest_framework import viewsets
from users import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication
from rest_framework import permissions
from rest_framework import mixins
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwnerOrReadOnly

User = get_user_model()


class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class UserViewSet(mixins.ListModelMixin,mixins.DestroyModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    retrieve：
        用户详情
    create：
        用户注册
    """
    queryset = models.DnsUserProfile.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    # 根据不同请求和权限，返回对应的信息
    def get_serializer_class(self):
        if self.action == "retrieve":
            if self.request.user.is_staff:
                return serializers.UserDetailSerializer
            return serializers.UserPersonalSerializer
        if self.action == "update":
            if self.request.user.is_staff:
                return serializers.UserDetailSerializer
            return serializers.UserPersonalSerializer
        elif self.action == "create":
            return serializers.UserRegSerializer

        return serializers.UserPersonalSerializer

    def get_permissions(self):
        """
            获取用户权限,用户只能获取自己的信息
        """
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        # if self.action == "list":
        #     return [IsOwnerOrReadOnly()]
        elif self.action == "create":
            return []

        return []

    def create(self, request, *args, **kwargs):
        """
            注册用户
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username
        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def get_object(self):
        """
            return: 当前用户
        """
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()


class ChangePassWordViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):

    serializer_class = serializers.ChangePassWordSerializer
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)

    def update(self, request, *args, **kwargs):
        """
            修改信息，修改人默认为当前用户
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.validated_data['update_user'] = self.request.user.username
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        """
            根据用户名查询，获取相关数据
        """
        queryset = User.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset