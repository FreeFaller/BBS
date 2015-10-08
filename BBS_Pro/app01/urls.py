__author__ = 'SunskyXH'
from django.conf.urls import include, url, patterns

import views

urlpatterns = patterns('',
                       (r'^$',views.index),
                       (r'^detail/(\d+)/$',views.bbs_detail),
                       (r'^sub_comment/$',views.sub_comment),
                       (r'^logout/$',views.logoutview),
                       (r'^bbs_pub/$',views.bbs_pub),
                       (r'^bbs_sub/$',views.bbs_sub),
                       (r'^category/(\d+)',views.category)
                       )