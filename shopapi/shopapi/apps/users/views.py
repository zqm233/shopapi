from rest_framework.response import Response
from rest_framework.views import APIView
from shopapi.libs.yuntongxun.sms import CCP
from .models import User
from rest_framework import status
from django.urls import re_path
import random
# Create your views here.


class SMSAPIView(APIView):
    def get(self, request):
        sms_code = random.randint(10000)
        ccp = CCP()
        result = ccp.send_template_sms('18782918728', ['1234', 5], 1)
        return Response(result)


class CheckMobileAPIView(APIView):
    def get(self,request,mobile):
        try:
            User.objects.get(mobile=mobile)
            result = False
            code = status.HTTP_400_BAD_REQUEST
        except User.DoesNotExist:
            result = True
            code = status.HTTP_200_OK
        return Response({'result':result},code)


