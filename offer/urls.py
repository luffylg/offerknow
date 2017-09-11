# -*- coding: utf-8 -*-
# __author__ = '40huo'
from django.conf.urls import url
from offer import views

urlpatterns = [
    url(r'^$', view=views.index, name='index'),
]