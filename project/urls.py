from django.conf.urls import include, url
from django.contrib import admin

from app.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    url(r'^app/', include('app.urls')),

#    url(r'^$', index),
#    url(r'^me$', me),
#    url(r'^health$', health),
#    url(r'^admin/', include(admin.site.urls)),
]
