# -*- coding: utf-8 -*-
from .models import Alias
from PublicMethod.allserializers import AllSerializer


class AliasSerializer(AllSerializer):
    """
    序列化 Models.Alias
    """

    class Meta:
        model = Alias
        fields = (
            '__all__'
        )


class AliasSerializer1(AllSerializer):
    """
    URL 传参 alias_method = 1 时，不序列化 old_ip 字段
    """

    class Meta:
        model = Alias
        fields = (
            'start_ip',
            'end_ip',
            'new_ip',
            'ipmask',
            'create_time',
            'update_time',
            'create_user',
            'update_user',
            'agentid',
            'remarks'
        )


class AliasSerializer2(AllSerializer):
    """
    URL 传参 alias_method = 2 时，不序列化 start_ip/end_ip 字段
    """

    class Meta:
        model = Alias
        fields = (
            'old_ip',
            'new_ip',
            'ipmask',
            'create_time',
            'update_time',
            'create_user',
            'update_user',
            'agentid',
            'remarks'
        )

