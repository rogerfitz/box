from django.conf.urls import patterns, url

from boxes import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.addBox, name='addBox'),
    url(r'^delete/(?P<box_id>\d+)/$', views.deleteBox, name='deleteBox'),
)
