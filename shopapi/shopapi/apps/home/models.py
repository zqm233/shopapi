from django.db import models

# Create your models here.
class Banner(models.Model):
    image = models.ImageField(upload_to='banner', verbose_name='轮播图', null=True, blank=True,help_text='图片大小 1920*720')
    name = models.CharField(max_length=50,verbose_name='轮播图名称')
    note = models.CharField(max_length=150,verbose_name='轮播图说明')
    link = models.CharField(max_length=150,verbose_name='轮播图广告地址')
    order = models.IntegerField(verbose_name='显示顺序')
    is_show = models.BooleanField(verbose_name='是否显示',default=False)
    is_del = models.BooleanField(verbose_name='逻辑删除',default=False)

    class Meta:
        db_table='shop_banner'
        verbose_name = '轮播图'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name