from django.db import models


class BaseModel(models.Model):
    order = models.IntegerField(verbose_name='显示顺序')
    is_show = models.BooleanField(verbose_name='是否显示', default=True)
    is_del = models.BooleanField(verbose_name='逻辑删除', default=False)
    created_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_time = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='发布时间')

    class Meta:
        abstract = True



