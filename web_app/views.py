from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import *
from .forms import UserRegisterForm, UserLoginForm

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def contact(request):
    return render(request, 'contact.html', {})

class VenueList(generic.ListView):

    if not request.user.is_authenticated():
        return render(request, 'login.html')

    template_name = 'venues.html'

    def get_queryset(self):
    	return Venue.objects.all()


class EventCampaignList(generic.ListView):

    if not request.user.is_authenticated():
        return render(request, 'login.html')

    template_name = 'eventcampaigns.html'

    def get_queryset(self):
    	return Event_campaign.objects.all()


class DetailViewVenue(generic.DetailView):

    if not request.user.is_authenticated():
        return render(request, 'login.html')

	model = Venue
	template_name = 'venue_detail.html'

 
class DetailViewEvent(generic.DetailView):

    if not request.user.is_authenticated():
        return render(request, 'login.html')

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

class EventCampaignDelete(DeleteView):
    model = Event_campaign
    success_url = reverse_lazy('index')

class VenueDelete(DeleteView):
    model = Venue
    success_url = reverse_lazy('index')

class RegisterView(View):
    form_class = UserRegisterForm
    template_name = 'web_app/register_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
        
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
        
            if user is not None:
                
                if user.is_active:
                    auth_login(request, user)
                    return redirect('index.html')

        return render(request, self.template_name, {'form' : form})

class LoginView(View):
    form_class = UserLoginForm
    template_name = 'web_app/login_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
        
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect('index.html')

        return render(request, self.template_name, {'form' : form})

def logout_user(request):
    template_name = 'web_app/login_form.html'
    logout(request)
    form = UserLoginForm(request.POST or None)

    return render(request, 'web_app/login_form.html', {'form' : form})









