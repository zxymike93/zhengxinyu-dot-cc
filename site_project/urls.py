"""
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from blog import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<page>\d*)/$', views.list),
    url(r'^$', views.list, name='list'),
    url(r'^(?P<slug>[\w\d-]+)/$', views.detail, name='detail'),
]

handler404 = 'site_project.views.handler404'
