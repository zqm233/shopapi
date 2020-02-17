from rest_framework import serializers
from .models import User
import re


class UserModelSerializer(serializers.ModelSerializer):
    sms_code = serializers.CharField(label='手机验证码', required=True, allow_null=False, allow_blank=False, write_only=True)
    password2 = serializers.CharField(label='确认密码', required=True, allow_null=False, allow_blank=False, write_only=True)

    class Meta:
        model = User
        fields = ['sms_code', 'mobile', 'password', 'password2']
        write_only_fields = ['password', 'password2', 'sms_code']

    def validate(self, attrs):

        if not re.match(r'^1[3-9]\d{9}$',attrs.get('mobile')):
            raise serializers.ValidationError('手机格式错误')

        try:
            User.objects.get(mobile=attrs.get('mobile'))
            raise serializers.ValidationError('手机号已注册')
        except:
            pass
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if len(password)<6:
            raise serializers.ValidationError('密码太短')
        if password != password2:
            raise serializers.ValidationError('密码不一致')

        return attrs

    def create(self, validated_data):
        del validated_data['password2']
        del validated_data['sms_code']
        validated_data['username'] = validated_data['mobile']
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user











