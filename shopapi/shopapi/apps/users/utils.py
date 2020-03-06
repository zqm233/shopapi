from django.contrib.auth.backends import ModelBackend
import re
from .models import User
from django_redis import get_redis_connection

def get_user_by_username(username):
    try:
        if re.match('^1[3-9]\d{9}$', username):
            print('1')
            user = User.objects.get(mobile=username)
        else:
            user = User.objects.get(username=username)

    except User.DoesNotExist:
        return None
    else:
        return user


def jwt_response_payload_handler(token,user=None,request=None):
    redis_con = get_redis_connection('cart')
    cart_num = redis_con.hlen('cart_%s'% user.id)

    return {
        'token':token,
        'id':user.id,
        'username':user.username,
        'cart_num':cart_num
    }


class UsernameMobileAuthBacked(ModelBackend):

    """
    自定义的用户认证
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = get_user_by_username(username)
        if user is None:
            return None
        if user.check_password(password) and self.user_can_authenticate(user):
            return user

