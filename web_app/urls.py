from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.venue_list, name='venue_list'),
    url(r'^index$', views.index, name='index'),
    url(r'^login$', views.login, name='login')
    url(r'^venues$', views.venue_list, name='venue_list'),
    url(r'^eventcampaigns$', views.event_campaign_list, name='event_campaign_list'),
]
