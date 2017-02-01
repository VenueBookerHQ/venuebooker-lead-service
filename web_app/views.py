from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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


class DetailView(generic.DetailView):
	model = Venue
	template_name = 'detail.html' 



def event_campaign_list(request):
    event_campaigns = Event_campaign.objects.order_by('pk')

    if len(event_campaigns) == 0:
        event_campaigns = {}

    return render(request, 'eventcampaigns.html', {'event_campaigns': event_campaigns})


class VenueCreate(CreateView):
	model = Venue
	fields = ['name', 'type', 'description', 'image']
