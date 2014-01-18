from django.conf.urls import patterns, url

from surveys import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.createSurvey, name='createSurvey'),
    #url(r'^delete/(?P<box_id>\d+)/$', views.deleteBox, name='deleteBox'),
)
