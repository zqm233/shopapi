from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from course.models import Course
from rest_framework.response import Response
from django_redis import get_redis_connection
from rest_framework import status
class CartAPIView(ViewSet):
    permission_classes = [IsAuthenticated]

    def add(self, request):
        course_id = request.data.get('course_id')
        user_id = request.user.id

        selected = True
        expire = 0

        try:
            course = Course.objects.filter(is_del=False, is_show=True, id=course_id)
        except Course.DoesNotExist:
            return Response({'message': '课程不存在', 'status': status.HTTP_400_BAD_REQUEST})
        redis_con = get_redis_connection("cart")
        try:
            pipe = redis_con.pipeline()
            pipe.multi()
            pipe.hset('cart:%s' % user_id, course_id, expire)
            pipe.sadd('selected_%s' % user_id, course_id)
            pipe.execute()
            cart_num = redis_con.hlen('cart:%s' % user_id)
        except:
            return Response({"message":"参数有误!购物车添加商品失败!"}, status=status.HTTP_507_INSUFFICIENT_STORAGE)

        return Response({'cart_num': cart_num, 'status': status.HTTP_201_CREATED})

    pass
