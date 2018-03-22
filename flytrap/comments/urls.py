#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created by flytrap
from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comments'),
    url('^(?P<pk>\d+)$', views.CommentViewSet.as_view({'put': 'update', 'delete': 'destroy'}), name='comment'),
]
