from django.conf.urls import patterns, url

from products import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.addProduct, name='addProduct'),
    url(r'^purchase/(?P<product_id>\d+)/$', views.purchaseProduct, name='purchaseProduct'),
    url(r'^edit/(?P<product_id>\d+)/$', views.editProduct, name='editProduct'),
    url(r'^delete/(?P<product_id>\d+)/$', views.deleteProduct, name='deleteProduct'),
)
