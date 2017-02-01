from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def login(request):
    return render(request, 'login.html', {})


class VenueList(generic.ListView):
    template_name = 'venues.html'

    def get_queryset(self):
    	return Venue.objects.all()


class EventCampaignList(generic.ListView):
    template_name = 'eventcampaigns.html'

    def get_queryset(self):
    	return Event_campaign.objects.all()


class DetailViewVenue(generic.DetailView):
	model = Venue
	template_name = 'venue_detail.html'

 
class DetailViewEvent(generic.DetailView):
	model = Event_campaign
	template_name = 'event_campaign_detail.html'


class VenueCreate(CreateView):
	model = Venue
	fields = ['name', 'type', 'description', 'image']


class EventCampaignCreate(CreateView):
	model = Event_campaign
	fields = ['name', 'type', 'details', 'capacity', 'image']


class VenueUpdate(UpdateView):
	model = Venue
	fields = ['name', 'type', 'description', 'image']


class EventCampaignUpdate(UpdateView):
	model = Event_campaign
	fields = ['name', 'type', 'details', 'capacity', 'image']
