from django.urls import path
from .views import BannerListAPIView, NavListAPIView

urlpatterns = [
    path('banner/', BannerListAPIView.as_view()),
    path('nav/', NavListAPIView.as_view()),

]
