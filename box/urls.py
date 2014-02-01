from django.conf.urls import patterns, include, url
from box import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^home/', include('home.urls')),
    url(r'^boxman/products/', include('products.urls')),
    url(r'^boxman/users/', include('users.urls')),
    url(r'^boxman/boxes/', include('boxes.urls')),
    url(r'^boxman/attrs/', include('attr.urls')),
    url(r'^boxman/', views.index, name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'users/login.html'}),
    url(r'^logout/$', 'users.views.logout'),
    url(r'^captcha/', include('captcha.urls')),
    
)

