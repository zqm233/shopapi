from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from course.models import Course
from rest_framework.response import Response
from django_redis import get_redis_connection
from rest_framework import status
from shopapi.settings.constant import SERVER_IMAGE_URL

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
            return Response({"message": "参数有误!购物车添加商品失败!"}, status=status.HTTP_507_INSUFFICIENT_STORAGE)

        return Response({'cart_num': cart_num, 'status': status.HTTP_201_CREATED})

    def delete(self, request):
        user_id = request.user.id
        course_id = request.query_params.get('course_id')
        redis_con = get_redis_connection('cart')
        redis_con.hdel('cart:%s' % user_id, course_id)
        redis_con.srem('selected%s' % user_id, course_id)
        return Response({'message': '删除成功'}, status.HTTP_200_OK)


    def patch(self, request):
        pass

    def put(self, request):
        user_id = request.user.id
        course_id = request.data.get('course_id')
        selected = request.data.get('selected')
        redis_con = get_redis_connection('cart')
        if selected:
            redis_con.srem('selected_%s' % user_id, course_id)
        else:
            redis_con.sadd('selected_%s' % user_id, course_id)

        return Response({'message':'商品勾选切换成功'}, status.HTTP_200_OK)

    def get(self, request):
        user_id = request.user.id
        redis_con = get_redis_connection('cart')
        cart_course_list = redis_con.hgetall('cart:%s' % user_id)
        cart_course_selected = redis_con.smembers('selected_%s' % user_id)

        if len(cart_course_list)<1:
            return Response([])
        data = []
        for course_id, expire in cart_course_list.items():
            try:
                course = Course.objects.get(pk=course_id)
                print(SERVER_IMAGE_URL + course.course_image.url)
            except: Course.DoesNotExist
            data.append({
                'course_id': course_id,
                'course_image': SERVER_IMAGE_URL + course.course_image.url,
                'course_name': course.name,
                'selected': True if course_id in cart_course_selected else False,
                'price': course.price

            })
            return Response(data)