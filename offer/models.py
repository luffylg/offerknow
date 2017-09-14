from django.db import models


# Create your models here.
class Offer(models.Model):
    """
    offer 类
    """
    RESULT_CHOICES = (
        ('unknown', '待定'),
        ('rejected', '回绝'),
        ('accepted', '收到 offer'),
    )

    company = models.CharField(verbose_name='公司', max_length=64)
    url = models.CharField(verbose_name='网址', max_length=256)
    application_date = models.DateField(verbose_name='申请日期')
    status = models.CharField(verbose_name='状态', max_length=32)
    last_interview_date = models.DateField(verbose_name='最后更新时间')
    application_method = models.CharField(verbose_name='申请渠道', max_length=64)
    result = models.CharField(verbose_name='结果', max_length=64, choices=RESULT_CHOICES)
