from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^newsletter$', views.newsletter, name='newsletter'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout_user, name='logout_user'),
    url(r'^register/$', views.register, name='register'),
    url(r'^terms$', views.terms, name='terms'),
    url(r'^privacy$', views.privacy, name='privacy'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^venues/$', views.venue_list, name='venue_list'),
    url(r'^venues/(?P<pk>[0-9]+)/$', login_required(views.DetailViewVenue.as_view()), name='venue_detail'),
    url(r'^venues/add/$', login_required(views.VenueCreate.as_view()), name='venue-add'),
    url(r'^venues/update/(?P<pk>[0-9]+)/$', login_required(views.VenueUpdate.as_view()), name='venue-update'),  
    url(r'^venues/(?P<pk>[0-9]+)/delete/$', login_required(views.VenueDelete.as_view()), name='venue-delete'),
    url(r'^organisations/$', views.organisation_list, name='organisation_list'),
    url(r'^organisations/(?P<pk>[0-9]+)/$', login_required(views.DetailViewOrganisation.as_view()), name='organisation_detail'),
    url(r'^organisations/add/$', login_required(views.OrganisationCreate.as_view()), name='organisation-add'),
    url(r'^organisations/update/(?P<pk>[0-9]+)/$', login_required(views.OrganisationUpdate.as_view()), name='organisation-update'),  
    url(r'^organisations/(?P<pk>[0-9]+)/delete/$', login_required(views.OrganisationDelete.as_view()), name='organisation-delete'),
    url(r'^eventcampaigns/$', views.event_list, name='event_campaign_list'),
    url(r'^eventcampaigns/(?P<pk>[0-9]+)/$', login_required(views.DetailViewEvent.as_view()), name='event_campaign_detail'),
    url(r'^eventcampaigns/(?P<pk>[0-9]+)/enquiry/$', login_required(views.EnquiryCreate.as_view()), name='enquiry-add'),
    url(r'^eventcampaigns/add/$', login_required(views.EventCampaignCreate.as_view()), name='event_campaign-add'), 
    url(r'^eventcampaigns/update/(?P<pk>[0-9]+)/$', login_required(views.EventCampaignUpdate.as_view()), name='event_campaign-update'), 
    url(r'^eventcampaigns/(?P<pk>[0-9]+)/delete/$', login_required(views.EventCampaignDelete.as_view()), name='event_campaign-delete'),
    url(r'^profile/(?P<pk>[0-9]+)/$', login_required(views.ProfileView.as_view()), name='profile'),
    url(r'^profile/update/(?P<pk>[0-9]+)/$', login_required(views.ProfileUpdate.as_view()), name='profile-update'),
    url(r'^quote/accept/(?P<pk>[0-9]+)/$', login_required(views.QuoteAccept.as_view()), name='quote-accept'),
    url(r'^quote/decline/(?P<pk>[0-9]+)/$', login_required(views.QuoteDecline.as_view()), name='quote-decline'),
]
