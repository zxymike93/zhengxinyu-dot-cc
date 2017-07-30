from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from blog import views as blog_view
from note import urls as note_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^note/', include(note_urls, namespace='note')),
    url(r'^(?P<page>\d*)/$', blog_view.list),
    url(r'^$', blog_view.list, name='list'),
    url(r'^(?P<slug>[\w\d-]+)/$', blog_view.detail, name='detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'site_project.views.handler404'
handler500 = 'site_project.views.handler500'
