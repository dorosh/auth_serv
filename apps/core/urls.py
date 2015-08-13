#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
    apps.core.urls
    ~~~~~~~~~

    :copyright: (c) 2015 by dorosh.
"""

__author__ = 'dorosh'
__date__ = '02.08.2015'


from django.conf.urls import patterns, include, url
from apps.core.views import Home, Index


urlpatterns = patterns(
    '', url(r'^$', Index.as_view(), name='index'),
    url(r'^home/$', Home.as_view(), name='home'),
)
