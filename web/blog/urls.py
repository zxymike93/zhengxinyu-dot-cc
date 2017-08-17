from django.conf.urls import url

from blog import views


urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^post/(?P<slug>[\w\d-]+)$', views.detail, name='detail'),
]
