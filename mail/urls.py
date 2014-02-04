from django.conf.urls import patterns, url

from mail import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='list'),
)
