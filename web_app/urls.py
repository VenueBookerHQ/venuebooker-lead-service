from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login_user'),
    url(r'^logout$', views.logout_user, name='logout_user'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^terms$', views.terms, name='terms'),
    url(r'^privacy$', views.privacy, name='privacy'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^venues/$', views.venue_list, name='venue_list'),
    url(r'^venues/(?P<pk>[0-9]+)/$', views.DetailViewVenue.as_view(), name='venue_detail'),
    url(r'^venues/add/$', views.VenueCreate.as_view(), name='venue-add'),
    url(r'^venues/update/(?P<pk>[0-9]+)/$', views.VenueUpdate.as_view(), name='venue-update'),  
    url(r'^venues/(?P<pk>[0-9]+)/delete/$', views.VenueDelete.as_view(), name='venue-delete'),
    url(r'^organisations/$', views.organisation_list, name='organisation_list'),
    url(r'^organisations/(?P<pk>[0-9]+)/$', views.DetailViewOrganisation.as_view(), name='organisation_detail'),
    url(r'^organisations/add/$', views.OrganisationCreate.as_view(), name='organisation-add'),
    url(r'^organisations/update/(?P<pk>[0-9]+)/$', views.OrganisationUpdate.as_view(), name='organisation-update'),  
    url(r'^organisations/(?P<pk>[0-9]+)/delete/$', views.OrganisationDelete.as_view(), name='organisation-delete'),
    url(r'^eventcampaigns/$', views.event_list, name='event_campaign_list'),
    url(r'^eventcampaigns/(?P<pk>[0-9]+)/$', views.DetailViewEvent.as_view(), name='event_campaign_detail'),
    url(r'^eventcampaigns/(?P<pk>[0-9]+)/enquiry/$', views.EnquiryCreate.as_view(), name='enquiry-add'),
    url(r'^eventcampaigns/add/$', views.EventCampaignCreate.as_view(), name='event_campaign-add'), 
    url(r'^eventcampaigns/update/(?P<pk>[0-9]+)/$', views.EventCampaignUpdate.as_view(), name='event_campaign-update'), 
    url(r'^eventcampaigns/(?P<pk>[0-9]+)/delete/$', views.EventCampaignDelete.as_view(), name='event_campaign-delete'),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.ProfileView.as_view(), name='profile'),
    url(r'^profile/update/(?P<pk>[0-9]+)/$', views.ProfileUpdate.as_view(), name='profile-update'),
]
