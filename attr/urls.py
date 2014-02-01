from django.conf.urls import patterns, url

from attr import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='list'),
    url(r'^add/$', views.addVertical, name='addVertical'),
    url(r'^deleteVertical/(?P<vert_id>\d+)/$', views.deleteVertical, name='deleteVertical'),  
    url(r'^addType/$', views.addType, name='addType'),
    url(r'^deleteType/(?P<type_id>\d+)/$', views.deleteType, name='deleteType'),  

)

