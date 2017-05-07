from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken import views
from web_app.viewsets import *

import web_app.views

admin.autodiscover()

# Examples:
# url(r'^$', 'base_site.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'organisations', OrganisationViewSet)
router.register(r'eventcampaigns', Event_campaignViewSet)
router.register(r'venues', VenueViewSet)
router.register(r'contactresponses', ContactResponseViewSet)
router.register(r'enquiries', EnquiryViewSet)
router.register(r'quotes', QuoteViewSet)
router.register(r'event_types', Event_typeViewSet)
router.register(r'leads', LeadViewSet)
router.register(r'rooms', RoomViewSet)

urlpatterns = [
    url(r'^$', web_app.views.index, name='index'),
    url(r'^web_app/', include('web_app.urls')),
    url(r'', include('web_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social_django.urls', namespace='social')),
    #url(r'^\.well-known/', include('letsencrypt.urls')),

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^admin/django-ses/', include('django_ses.urls')),
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
