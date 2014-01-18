from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='list'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^add/$', views.addUser, name='addUser'),
    url(r'^delete/(?P<user_id>\d+)/$', views.deleteUser, name='deleteUser'),
    url(r'^assignBox/(?P<prof_id>\d+)/$', views.assignBox, name='assignBox'),
)
