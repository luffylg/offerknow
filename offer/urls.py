# -*- coding: utf-8 -*-
# __author__ = '40huo'
from django.conf.urls import url

from offer import views

app_name = 'offer'
urlpatterns = [
    url(r'^$', view=views.index, name='index'),
]
