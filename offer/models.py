from django.db import models


# Create your models here.
class Offer(models.Model):
    company = models.CharField('公司', max_length=64)
    url = models.CharField('网址', max_length=256)
    application_date = models.DateField('申请日期', auto_now_add=True)
    status = models.CharField('状态', max_length=32)
    last_interview_date = models.DateField('最后更新时间', auto_now_add=True)
    application_method = models.CharField('申请渠道', max_length=64)
    result = models.CharField('结果', max_length=64)
