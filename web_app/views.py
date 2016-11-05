from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from web_app.models import Venue

def index(request):
    venues = Venue.objects.order_by('priority')

    return render(request, 'index.html', {'venues': venues})


def venue_list(request):
    venues = Venue.objects.order_by('priority')

    if len(venues) == 0:
        venues = {}

    return render(request, 'index.html', {'venues': venues})
