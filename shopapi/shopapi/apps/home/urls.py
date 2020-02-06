from django.urls import path,re_path
from .views import BannerListAPIView

urlpatterns=[
    path('banner/',BannerListAPIView.as_view()),
]