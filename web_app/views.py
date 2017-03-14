from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import *
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def contact(request):
    return render(request, 'contact.html', {})


class DetailViewVenue(generic.DetailView):
    model = Venue
    template_name = 'venue_detail.html'

class DetailViewEvent(generic.DetailView):
    model = Event_campaign
    template_name = 'event_campaign_detail.html'

class DetailViewOrganisation(generic.DetailView):
    model = Organisation
    template_name = 'organisation_detail.html'

class ProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'profile.html'


class VenueCreate(CreateView):
    model = Venue
    fields = ['name', 'address', 'facebook_link', 'twitter_link', 'instagram_link', 'description', 'organisation', 'image']


class VenueUpdate(UpdateView):
    model = Venue
    fields = ['name', 'address', 'facebook_link', 'twitter_link', 'instagram_link', 'description', 'image']

class VenueDelete(DeleteView):
    model = Venue
    success_url = reverse_lazy('index')

class OrganisationCreate(CreateView):
    model = Organisation
    fields = ['name', 'image', 'address', 'primary_contact', 'description']

class OrganisationUpdate(UpdateView):
    model = Organisation
    fields = ['name', 'image', 'address', 'primary_contact', 'description']

class OrganisationDelete(DeleteView):
    model = Organisation
    success_url = reverse_lazy('index')


class EventCampaignCreate(CreateView):
    model = Event_campaign
    fields = ['name', 'type', 'details', 'startTime', 'endTime', 'recurring', 'capacity', 'cost_per_capacity_unit', 'venue', 'image']

class EventCampaignUpdate(UpdateView):
    model = Event_campaign
    fields = ['name', 'type', 'details', 'startTime', 'endTime', 'recurring', 'capacity', 'cost_per_capacity_unit', 'venue', 'image']

class EventCampaignDelete(DeleteView):
    model = Event_campaign
    success_url = reverse_lazy('index')

class EnquiryCreate(CreateView):
    model = Enquiry
    fields = ['message', 'attendeeNum', 'date']
    success_url = "/eventcampaigns"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.event_campaign = get_object_or_404(Event_campaign, pk=self.kwargs['pk'])
        form.save()
        return super(EnquiryCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('event_campaign_detail', kwargs={'pk':self.kwargs['pk']})

class RegisterView(View):
    form_class = UserForm
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
            
            g = Group.objects.get(name='VenueAdmin') 
            g.user_set.add(your_user)
        
            if user is not None:
                
                if user.is_active:
                    auth_login(request, user)
                    return redirect('index')

        return render(request, self.template_name, {'form' : form})

#User Login View
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return render(request, 'index.html')
        else:
            return render(request, 'web_app/login_form.html')
    return render(request, 'web_app/login_form.html')

#User Logout View
def logout_user(request):
    template_name = 'web_app/login_form.html'
    logout(request)
    form = UserForm(request.POST or None)

    return render(request, 'web_app/login_form.html', {'form' : form})


class VenueDashView(generic.ListView):
    template_name = 'venuedash.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def get_queryset(self):
        return Event_campaign.objects.filter(venue=request.venue.name)

class OrganisationDashView(generic.ListView):
    template_name = 'organisationdash.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def get_queryset(self):
        return Venue.objects.filter(organisation=request.organisation.name)

def event_list(request):
    queryset_list = Event_campaign.objects.all()
    query = request.GET.get("search-query")
    if query:
        queryset_list = queryset_list.filter(name__icontains=query)
    paginator = Paginator(queryset_list, 10)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "title": "List",
    }
    return render(request, "eventcampaigns.html", context)

def venue_list(request):
    queryset_list = Venue.objects.all()
    query = request.GET.get("search-query")
    if query:
        queryset_list = queryset_list.filter(name__icontains=query)
    paginator = Paginator(queryset_list, 10)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "title": "List",
    }
    return render(request, "venues.html", context)

def organisation_list(request):
    queryset_list = Organisation.objects.all()
    query = request.GET.get("search-query")
    if query:
        queryset_list = queryset_list.filter(name__icontains=query)
    paginator = Paginator(queryset_list, 10)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "title": "List",
    }
    return render(request, "organisations.html", context)

