__author__ = 'SunskyXH'
from django.conf.urls import include, url, patterns

import views

urlpatterns = patterns('',
                       (r'^$',views.index))