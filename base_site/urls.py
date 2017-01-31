from django.conf.urls import include, url
from django.contrib import admin

import web_app.views

admin.autodiscover()

# Examples:
# url(r'^$', 'base_site.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', web_app.views.index, name='index'),
    url(r'^$venues/', web_app.views.venue_list, name='venue_list'),
    url(r'^$eventcampaigns/', web_app.views.event_campaign_list, name='event_campaign_list'),
    url(r'^web_app/', include('web_app.urls')),
    url(r'', include('web_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
