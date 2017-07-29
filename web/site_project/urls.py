from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from blog import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<page>\d*)/$', views.list),
    url(r'^$', views.list, name='list'),
    url(r'^(?P<slug>[\w\d-]+)/$', views.detail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'site_project.views.handler404'
handler500 = 'site_project.views.handler500'
