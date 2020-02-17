import random
from .serializer import UserModelSerializer
from django_redis import get_redis_connection
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from shopapi.libs.yuntongxun.sms import CCP
from .models import User


class SMSAPIView(APIView):
    def get(self, request,mobile):
        code = random.randint(10000)
        redis_con = get_redis_connection('sms_code')
        p1 = redis_con.pipeline()
        p1.multi()
        p1.setex("sms_%s" % mobile, 300, code)
        p1.setex("sms_time_%s" % mobile, 60, 1)
        p1.execute()
        ccp = CCP()
        result = ccp.send_template_sms('18782918728', [code, 5], 1)
        return Response(result)


class CheckMobileAPIView(APIView):
    def get(self, request, mobile):
        try:
            User.objects.get(mobile=mobile)
            result = False
            code = status.HTTP_400_BAD_REQUEST
        except User.DoesNotExist:
            result = True
            code = status.HTTP_200_OK
        return Response({'result': result}, code)


class UserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer



