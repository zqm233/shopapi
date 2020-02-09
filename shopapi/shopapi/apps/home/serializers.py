from rest_framework import serializers
from .models import Banner, Nav


class BannerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['image', 'link']


class NavModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nav
        fields = ['name', 'link', 'opt']
