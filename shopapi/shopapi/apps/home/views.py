from rest_framework.generics import ListAPIView
from.models import Banner
from shopapi.settings.constant import BANNER_LIMMIT
from .serializers import BannerModelSerializer
# Create your views here.
class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True,is_del=False).order_by('order')[:BANNER_LIMMIT]

    serializer_class = BannerModelSerializer

