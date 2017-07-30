from django.conf.urls import url

from note import views


urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^(?P<slug>[\w\d-]+)/$', views.detail, name='detail'),
]
