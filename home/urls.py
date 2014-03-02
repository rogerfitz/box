from django.conf.urls import patterns, url, include

from home import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^profiles/', views.editProfile, name='editProfile'),
    url(r'^preferences/', include('preferences.urls')),
    url(r'^ipn/', views.ipn, name='ipn'),
)
