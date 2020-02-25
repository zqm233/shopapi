from django.urls import path,re_path
from .views import SMSAPIView,CheckMobileAPIView
from rest_framework_jwt.views import obtain_jwt_token
from.views import UserAPIView

urlpatterns = [
    path('login/', obtain_jwt_token,),
    path('sms/', SMSAPIView.as_view()),
    re_path('mobile/(?P<mobile>1[3-9]\d{9})', CheckMobileAPIView.as_view()),
    path('register/',UserAPIView.as_view(),)


]

