from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import *
from .forms import UserForm, ContactForm, ContactResponseForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.forms import PasswordChangeForm
import boto3
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.http import is_safe_url
from django.template import *
from django.template.loader import get_template
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def contact(request):
    template_name = 'contact.html'
    template_html = 'emails/contact.html'
    template_text = 'emails/contact.txt'
    

    if request.method == 'POST':
        form = ContactResponseForm(request.POST)

        if form.is_valid():

            contactresponse = form.save(commit=False)
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            emailAddress = form.cleaned_data['email']
            vbemail = "gregwhyte14@gmail.com"
            message = form.cleaned_data['message']
            contactresponse.save()
            timestamp = contactresponse.timestamp.strftime('%H:%M %d-%m-%Y')
                 
            if request.method == 'POST':
                try:
                    subject = 'Contact Form Response'
                    from_email = 'Venuebooker Contact Response <gregwhyte14@gmail.com>'
                    to = vbemail
                    text = get_template(template_text)
                    html = get_template(template_html)
                    d = Context({'name': name, 'emailAddress': emailAddress, 'phone': phone, 'timestamp': timestamp, 'message': message})
                    text_content = text.render(d)
                    html_content = html.render(d)

                    email = EmailMultiAlternatives(subject, text_content, from_email, [to])
                    email.attach_alternative(html_content, "text/html") 
                    email.content_subtype = 'html'    
                    email.mixed_subtype = 'related'                        
                    email.send()
                except KeyError:
                    return HttpResponse('Please fill in all fields')
                   
            return redirect('index')

        return render(request, template_name, {})

    else:
        contactresponse_form = ContactResponseForm(None)
        return render(request, template_name, {})

def newsletter(request):
    template_html = 'emails/newsletter.html'
    template_text = 'emails/newsletter.txt'
    emailAddress = request.POST['email']
    try:
        subject = 'Subscribed to Veneubooker Newsletter'
        from_email = 'Venuebooker <gregwhyte14@gmail.com>'
        to = emailAddress
        text = get_template(template_text)
        html = get_template(template_html)
        d = Context({'email': to })
        text_content = text.render(d)
        html_content = html.render(d)

        email = EmailMultiAlternatives(subject, text_content, from_email, [to])
        email.attach_alternative(html_content, "text/html") 
        email.content_subtype = 'html'    
        email.mixed_subtype = 'related'                         
        email.send()
    except KeyError:
        return HttpResponse('Please fill in all fields')
    except Exception as e:
        return redirect('index')

    next = request.POST.get('next')
    if not is_safe_url(next):
        next = 'index'
    return redirect(next)

def terms(request):
    return render(request, 'terms.html', {})

def privacy(request):
    return render(request, 'privacy.html', {})

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


class ProfileUpdate(UpdateView):
    model = CustomUser
    fields = ['email', 'avatar']

    def get_success_url(self):
        return reverse('profile', kwargs={'pk':self.kwargs['pk']})

class VenueCreate(CreateView):
    model = Venue
    fields = ['name', 'address', 'facebook_link', 'twitter_link', 'instagram_link', 'description', 'organisation', 'image']
    success_url = "/venues"

    def form_valid(self, form):
        if hasattr(request.user, 'organisationuser'):
            form.instance.organisation = self.request.user.organisationuser.organisation         
        form.save()
        return super(VenueCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('event_campaign_detail', kwargs={'pk':self.kwargs['pk']})

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

class QuoteCreate(CreateView):
    model = Quote
    fields = ['description', 'cost']
    success_url = "/eventcampaigns"

    def form_valid(self, form):
        enquiry = get_object_or_404(Enquiry, pk=self.kwargs['pk'])
        form.instance.enquiry = enquiry
        form.save()
        try:
            subject = 'Quote Recieved'
            message = 'Hello ' + username + '\nYou have recieved a quote for the enquiry you made \n Regards, \n The Venuebooker Team'
            from_email = 'Venuebooker <gregwhyte14@gmail.com>'
            to = emailAddress
            text = get_template(template_text)
            html = get_template(template_html)
            d = Context({'username': username })
            text_content = text.render(d)
            html_content = html.render(d)

            email = EmailMultiAlternatives(subject, text_content, from_email, [to])
            email.attach_alternative(html_content, "text/html")  
            email.content_subtype = 'html'    
            email.mixed_subtype = 'related'                       
            email.send()
        except Exception as e:
            return redirect('index')
        return super(QuoteCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('event_campaign_detail', kwargs={'pk':self.kwargs['pk']})

def register(request):
    template_html = 'emails/register.html'
    template_text = 'emails/register.txt'
    template_name = 'web_app/register_form.html'
    

    if request.method == 'POST':
        #form = self.form_class(request.POST)
        user_form = UserForm(request.POST, request.FILES)
        contact_form = ContactForm(request.POST)

        if all([user_form.is_valid(), contact_form.is_valid()]):

            contact = contact_form.save(commit=False)
            user = user_form.save(commit=False)
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            emailAddress = contact_form.cleaned_data['email']
            user.email = emailAddress
            user.avatar = user_form.cleaned_data['avatar']
            user.set_password(password)
            contact.save()
            user.contact = contact
            user.save()

            user = authenticate(username=username, password=password)
            
        
            if user is not None:
                if request.method == 'POST':
                    try:
                        subject = 'Registered to Veneubooker'
                        from_email = 'Venuebooker <gregwhyte14@gmail.com>'
                        to = emailAddress
                        text = get_template(template_text)
                        html = get_template(template_html)
                        d = {'username': username }
                        text_content = text.render(d)
                        html_content = html.render(d)

                        email = EmailMultiAlternatives(subject, text_content, from_email, [to])
                        email.attach_alternative(html_content, "text/html")                        
                        email.send()
                    except KeyError:
                        return HttpResponse('Please fill in all fields')

                    if user.is_active:
                        auth_login(request, user)
                        return redirect('index')

        return render(request, template_name, {'user_form' : user_form, 'contact_form' : contact_form,})

    else:
        user_form = UserForm(None)
        contact_form = ContactForm(None)
        return render(request, template_name, {'user_form' : user_form, 'contact_form' : contact_form,})

#User Login View
def login(request):
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
@login_required(login_url='login')
def logout_user(request):
    template_name = 'web_app/login_form.html'
    logout(request)
    form = UserForm(request.POST or None)

    return render(request, 'web_app/login_form.html', {'form' : form})

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			messages.success(request, 'Your password was successfully changed!')
			return redirect('profile', pk=request.user.id)
		else:
			messages.error(request, 'Please correct the error')
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'web_app/change_password.html', {'form': form})

@login_required(login_url='login')
def event_list(request):
    queryset_list = Event_campaign.objects.all()
    query = request.GET.get("q")
    minCost = request.GET.get("min")
    maxCost = request.GET.get("max")
    minCap = request.GET.get("capmin")
    maxCap = request.GET.get("capmax")
    if query:
        queryset_list = queryset_list.filter(Q(name__icontains=query) | Q(venue__name__icontains=query))
    if minCost and maxCost:
        queryset_list = queryset_list.filter(cost_per_capacity_unit__gte = minCost, cost_per_capacity_unit__lte = maxCost)
    elif minCost and not maxCost:
        queryset_list = queryset_list.filter(cost_per_capacity_unit__gte = minCost)
    elif maxCost and not minCost:
        queryset_list = queryset_list.filter(cost_per_capacity_unit__lte = maxCost)
    if minCap and maxCap:
        queryset_list = queryset_list.filter(capacity__gte = minCap, capacity__lte = maxCap)
    elif minCap and not maxCap:
        queryset_list = queryset_list.filter(capacity__gte = minCap)
    elif maxCap and not minCap:
        queryset_list = queryset_list.filter(capacity__lte = maxCap)
    paginator = Paginator(queryset_list, 9)
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

@login_required(login_url='login')
def venue_list(request):
    queryset_list = Venue.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(name__icontains=query)
    paginator = Paginator(queryset_list, 9)
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

@login_required(login_url='login')
def organisation_list(request):
    queryset_list = Organisation.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(name__icontains=query)
    paginator = Paginator(queryset_list, 9)
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

class QuoteAccept(View):
    def post(self, request, pk):
        template_html = 'emails/quote_accepted.html'
        template_text = 'emails/quote_accepted.txt'
        quoteNum = pk
        Quote.objects.filter(pk=quoteNum).update(accepted=True)
        quote = Quote.objects.get(pk=quoteNum)
        try:
            subject = 'Quote Accepted'
            from_email = 'Venuebooker <gregwhyte14@gmail.com>'
            to = quote.enquiry.event_campaign.venue.organisation.primary_contact.email
            name = quote.enquiry.event_campaign.venue.organisation.primary_contact
            user = quote.enquiry.user.username
            text = get_template(template_text)
            html = get_template(template_html)
            d = Context({'user': user, 'name': name})
            text_content = text.render(d)
            html_content = html.render(d)

            email = EmailMultiAlternatives(subject, text_content, from_email, [to])
            email.attach_alternative(html_content, "text/html")  
            email.content_subtype = 'html'    
            email.mixed_subtype = 'related'                       
            email.send()
        except Exception as e:
            return HttpResponseRedirect('/index')
        url = reverse('profile', kwargs={'pk': request.user.id})
        return HttpResponseRedirect(url)

class QuoteDecline(View):
    def post(self, request, pk):
        quoteNum = pk
        Quote.objects.filter(pk=quoteNum).delete()
        url = reverse('profile', kwargs={'pk': request.user.id})
        return HttpResponseRedirect(url)
