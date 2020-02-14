from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    mobile = models.CharField(max_length=15,verbose_name='手机号码',unique=True)
    avatar = models.ImageField(upload_to='avatar',verbose_name='头像',blank=True,null=True,help_text='256*256')

    class Meta:
        db_table = 'shop_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
