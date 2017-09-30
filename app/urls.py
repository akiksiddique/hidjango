from django.conf.urls import patterns, url
from app.views import index,me,job
#from app import views

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^me/$', me, name='me'),
    url(r'^job/$', job),
    url(r'^mother/$', mother, name='mother'),    
)
