from django.db import models
from shopapi.utils.models import BaseModel
# Create your models here.


class Banner(BaseModel):
    image = models.ImageField(upload_to='banner', verbose_name='轮播图', null=True, blank=True, help_text='图片大小 1920*720')
    name = models.CharField(max_length=50, verbose_name='轮播图名称')
    note = models.CharField(max_length=150, verbose_name='轮播图说明')
    link = models.CharField(max_length=150, verbose_name='轮播图广告地址')


    class Meta:
        db_table = 'shop_banner'
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Nav(BaseModel):
    NAV_POSITION = (
        (1, 'top'),
        (2, 'footer')
    )

    name = models.CharField(max_length=50, verbose_name='导航项名称')
    link = models.CharField(max_length=150, verbose_name='导航地址')
    opt = models.SmallIntegerField(choices=NAV_POSITION, verbose_name='导航位置',default=1)

    class Meta:

        db_table = 'shop_nav'
        verbose_name = '导航'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
