from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^venues/$', views.VenueList.as_view(), name='venue_list'),
    url(r'^venues/(?P<pk>[0-9]+)/$', views.DetailViewVenue.as_view(), name='venue_detail'),
    url(r'^venues/add/$', views.VenueCreate.as_view(), name='venue-add'),
    url(r'^venues/update/(?P<pk>[0-9]+)/$', views.VenueUpdate.as_view(), name='venue-update'),  
    #url(r'^venues/(?P<pk>[0-9]+)/delete/$', views.VenueDelete.as_view(), name='venue-delete'),
    url(r'^eventcampaigns/$', views.EventCampaignList.as_view(), name='event_campaign_list'),
    url(r'^eventcampaigns/(?P<pk>[0-9]+)/$', views.DetailViewEvent.as_view(), name='event_campaign_detail'),
    url(r'^eventcampaigns/add/$', views.EventCampaignCreate.as_view(), name='event_campaign-add'), 
    url(r'^eventcampaigns/update/(?P<pk>[0-9]+)/$', views.EventCampaignUpdate.as_view(), name='event_campaign-update'), 
    url(r'^eventcampaigns/(?P<pk>[0-9]+)/delete/$', views.EventCampaignDelete.as_view(), name='event_campaign-delete'),
]
