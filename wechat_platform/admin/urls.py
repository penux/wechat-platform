# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^dashboard/', include('admin.dashboard.urls', namespace='dashboard')),
    url(r'^library/', include('admin.library.urls', namespace='library')),
    url(r'^user/', include('admin.user.urls', namespace='user')),
    url(r'^official_account/', include('admin.official_account.urls', namespace='official_account')),
)