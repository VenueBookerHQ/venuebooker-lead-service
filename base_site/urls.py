from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

import web_app.views

admin.autodiscover()

# Examples:
# url(r'^$', 'base_site.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', web_app.views.index, name='index'),
    url(r'^web_app/', include('web_app.urls')),
    url(r'', include('web_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
