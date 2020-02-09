from rest_framework.generics import ListAPIView
from .models import Banner, Nav
from shopapi.settings.constant import BANNER_LIMIT, NAV_LIMIT
from .serializers import BannerModelSerializer, NavModelSerializer


# Create your views here.


class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True, is_del=False).order_by('order')[:BANNER_LIMIT]
    serializer_class = BannerModelSerializer


class NavListAPIView(ListAPIView):
    queryset = Nav.objects.filter(is_show=True, is_del=False).order_by('order')[:NAV_LIMIT]
    serializer_class = NavModelSerializer

