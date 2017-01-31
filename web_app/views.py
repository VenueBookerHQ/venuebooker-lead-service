from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def login(request):
    return render(request, 'login.html', {})

def venue_list(request):
    venues = Venue.objects.order_by('pk')

    if len(venues) == 0:
        venues = {}

    return render(request, 'venues.html', {'venues': venues})


def event_campaign_list(request):
    event_campaigns = Event_campaign.objects.order_by('pk')

    if len(event_campaigns) == 0:
        event_campaigns = {}

    return render(request, 'eventcampaigns.html', {'eventcampaigns': event_campaigns})

