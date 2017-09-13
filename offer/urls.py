# -*- coding: utf-8 -*-
# __author__ = '40huo'
from django.conf.urls import url

from offer import views

app_name = 'offer'
urlpatterns = [
    url(r'^$', view=views.index, name='index'),
    url(r'^add-offer/$', view=views.add_offer, name='add_offer'),
    url(r'^edit/(?P<offer_id>\d+)/$', view=views.update_offer, name='edit_offer'),
    url(r'^delete/(?P<offer_id>\d+)/$', view=views.delete_offer, name='delete_offer'),
]
