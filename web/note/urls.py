from django.conf.urls import url

from note import views


urlpatterns = [
    url(r'^(?P<category>[\w]*)$', views.list, name='list'),
    url(r'^post/(?P<slug>[\w\d-]+)$', views.detail, name='detail'),
]
