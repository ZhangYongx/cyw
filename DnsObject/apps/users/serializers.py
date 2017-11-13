# -*- coding: utf-8 -*-
import re
from rest_framework import serializers
from users import models
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from DnsObject.settings import REGEX_MOBILE

User = get_user_model()


# class ChangePasswordSerializer(serializers.ModelSerializer):

class UserDetailSerializer(serializers.ModelSerializer):
    """
        用户详细信息serializers
    """
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    def validate_mobile(self, mobile):
        """
        验证手机号码
        """

        # 手机是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("该手机号已被注册！")

        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码非法！")
        return mobile

    class Meta:
        model = models.DnsUserProfile
        fields = (
            '__all__'
        )
        read_only_fields = ('create_user', 'update_user',)


class UserPersonalSerializer(serializers.ModelSerializer):
    """
           用户基本信息serializers
    """
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    mobile = serializers.CharField(required=True, max_length=11, label="电话", help_text="请输入手机号")

    def validate_mobile(self, mobile):
        """
        验证手机号码
        """

        # 手机是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("该手机号已被注册！")

        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码非法！")
        return mobile

    class Meta:
        model = User
        fields = ("id", "username", "name", "mobile", "qq", "email", "update_time")
        read_only_fields = ('username', )


class UserRegSerializer(serializers.ModelSerializer):
    """
        用户注册serializers
    """
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])
    password = serializers.CharField(
        style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True,
    )

    mobile = serializers.CharField(required=True, max_length=11, label="电话", help_text="请输入手机号")

    def validate_mobile(self, mobile):
        """
        验证手机号码
        """

        # 手机是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("该手机号已被注册！")

        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码非法！")
        return mobile

    class Meta:
        model = User
        fields = ("id", "username", "password", "mobile", "email")


class ChangePassWordSerializer(serializers.ModelSerializer):
    oldpassword = serializers.CharField(style={'input_type': 'password'}, help_text="请输入原始密码", label="密码",
                                        write_only=True)
    newpassword = serializers.CharField(style={'input_type': 'password'}, help_text="请输入新密码", label="新密码",
                                        write_only=True)
    ConfirmationPassword = serializers.CharField(style={'input_type': 'password'}, help_text="请再次输入",
                                                 label="确认密码", write_only=True)
    # username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
    #                                  validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])
    # password = serializers.CharField(
    #     style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True,
    # )

    def update(self, instance, validated_data):
        verify_records = models.DnsUserProfile.objects.filter(username=self.initial_data['username'])
        user = super(ChangePassWordSerializer,self).update(instance, validated_data=validated_data)
        if verify_records.password == validated_data['oldpassword']:
            newpassword = validated_data['newpassword']
            user.set_password(newpassword)
            user.save()
            return user


    def validate(self, attrs):
        del attrs["oldpassword"]
        del attrs["newpassword"]
        del attrs["ConfirmationPassword"]
        return attrs

    class Meta:
        model = User
        fields = ("id", "username", "oldpassword", "newpassword", "ConfirmationPassword")
        # read_only_fields = ('username',)