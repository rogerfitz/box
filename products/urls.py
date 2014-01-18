from django.conf.urls import patterns, url

from products import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.addProduct, name='addProduct'),
    url(r'^delete/(?P<box_id>\d+)/$', views.deleteProduct, name='deleteProduct'),
)
