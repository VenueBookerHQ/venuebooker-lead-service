from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

# Url Patterns used for directing to views in the views.py file
# Url patterns act as almost a controller in the traditional MVC pattern
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^newsletter$', views.newsletter, name='newsletter'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout_user, name='logout_user'),
    url(r'^register/$', views.register, name='register'),
	url(r'^password/$', views.change_password, name='change_password'),
    url(r'^terms$', views.terms, name='terms'),
    url(r'^privacy$', views.privacy, name='privacy'),
    url(r'^about$', views.about, name='about'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^venues/$', views.venue_list, name='venue_list'),
    url(r'^venues/(?P<pk>[0-9]+)/$', views.venue_view, name='venue_detail'),
    url(r'^venues/add/$', views.venue_create, name='venue-add'),
	url(r'^venues/signup/$', views.venue_signup_info, name='venue_signup_info'),
    url(r'^eventcampaigns/$', views.event_list, name='event_campaign_list'),
    url(r'^eventcampaigns/(?P<pk>[0-9]+)/$', views.event_campaign_view, name='event_campaign_detail'),
    url(r'^eventcampaigns/(?P<pk>[0-9]+)/enquiry/$', login_required(views.EnquiryCreate.as_view()), name='enquiry-add'),
    url(r'^profile/$', views.profile_view, name='profile'),
    url(r'^profile/update/$', views.update_profile, name='profile-update'),
    url(r'^quote/accept/(?P<pk>[0-9]+)/$', login_required(views.QuoteAccept.as_view()), name='quote-accept'),
    url(r'^quote/decline/(?P<pk>[0-9]+)/$', login_required(views.QuoteDecline.as_view()), name='quote-decline'),
]
