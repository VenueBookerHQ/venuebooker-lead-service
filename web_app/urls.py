from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^venues/$', views.VenueList.as_view(), name='venue_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^eventcampaigns/$', views.event_campaign_list, name='event_campaign_list'),
]
