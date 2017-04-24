from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import *
from .forms import UserForm, ContactForm, ContactResponseForm, ProfileForm, CustomUserChangeForm, VenueForm
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

#Index view for web platform
def index(request):
	return render(request, 'index.html', {})

#View for information about venue signup, preceeds venue add process
def venue_signup_info(request):
	return render(request, 'venue_signup.html', {})

#View used for contact response form, sends email to company contact email with contact message and details
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
			vbemail = "contact@venuebooker.com"
			message = form.cleaned_data['message']
			contactresponse.save()
			timestamp = contactresponse.timestamp.strftime('%H:%M %d-%m-%Y')
				 
			if request.method == 'POST':
				try:
					subject = 'Contact Form Response'
					from_email = 'Venuebooker Contact Response <contact@venuebooker.com>'
					to = vbemail
					text = get_template(template_text)
					html = get_template(template_html)
					d = {'name': name, 'emailAddress': emailAddress, 'phone': phone, 'timestamp': timestamp, 'message': message}
					text_content = text.render(d)
					html_content = html.render(d)

					email = EmailMultiAlternatives(subject, text_content, from_email, [to])
					email.attach_alternative(html_content, "text/html") 
					email.content_subtype = 'html'	
					email.mixed_subtype = 'related'						
					email.send()
				except KeyError:
					return HttpResponse('Please fill in all fields')
				   
			messages.success(request, 'Thanks for contacting us. We will be in touch with you shortly.')
			return HttpResponseRedirect(reverse(contact))

		return render(request, template_name, {'form': form})

	else:
		contactresponse_form = ContactResponseForm(None)
		return render(request, template_name, {})

#View used for newsletter signup
def newsletter(request):
	template_html = 'emails/newsletter.html'
	template_text = 'emails/newsletter.txt'
	emailAddress = request.POST['email']
	try:
		subject = 'Subscribed to Veneubooker Newsletter'
		from_email = 'Venuebooker <noreply@venuebooker.com>'
		to = emailAddress
		text = get_template(template_text)
		html = get_template(template_html)
		d = {'email': to }
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

#Terms and conditions view
def terms(request):
	return render(request, 'terms.html', {})

#Privacy policy view
def privacy(request):
	return render(request, 'privacy.html', {})

#View for viewing a venue, venue based on request pk, redirect if not approved venue
@login_required(login_url='login')
def venue_view(request, pk):
	venuepk = pk
	venueObj = get_object_or_404(Venue, pk=venuepk)
	eventqueryset = Event_campaign.objects.filter(venue=venueObj)
	context = {
		"venue": venueObj,
		"event_list": eventqueryset,
	}
	if venueObj.approved:
		return render(request, "venue_detail.html", context)
	else:
		return render(request, "index.html")

#View for viewing an event campaign, gets event campaign based on request pk
@login_required(login_url='login')
def event_campaign_view(request, pk):
	eventpk = pk
	eventObj = get_object_or_404(Event_campaign, pk=eventpk)
	context = {
		"event_campaign": eventObj,
	}
	return render(request, "event_campaign_detail.html", context)

#View for viewing the users profile, requires login 
@login_required(login_url='login')
def profile_view(request):
	profilepk = request.user.id
	userObj = get_object_or_404(CustomUser, pk=profilepk)
	context = {
		"user": userObj,
	}
	return render(request, "profile.html", context)

#View for updating user profile with information entered in the form, Using Profile and Contact Forms, requires login
@login_required(login_url='login')
def update_profile(request):
	template_name = 'web_app/customuser_form.html'

	if request.method == 'POST':
		user_form = ProfileForm(data=request.POST, files=request.FILES, instance=request.user)
		contact_form = ContactForm(data=request.POST, instance=request.user.contact)

		if all([user_form.is_valid(), contact_form.is_valid()]):
			contact = contact_form.save(commit=False)
			user = user_form.save()
			emailAddress = contact_form.cleaned_data['email']
			user.email = emailAddress
			user.avatar = user_form.cleaned_data['avatar']
			contact.save()
			user.contact = contact
			user.save()
			return redirect('profile')

		return render(request, template_name, {'user_form' : user_form, 'contact_form' : contact_form,})

	else:
		user_form = ProfileForm(instance=request.user)
		contact_form = ContactForm(instance=request.user.contact)
		return render(request, template_name, {'user_form' : user_form, 'contact_form' : contact_form,})

#View for creating a venue, requires login
@login_required(login_url='login')
def venue_create(request):
	template_name = 'web_app/venue_form.html'

	if request.method == 'POST':
		venue_form = VenueForm(data=request.POST, files=request.FILES)

		if venue_form.is_valid():
			venue = venue_form.save(commit=False)
			venue.image = venue_form.cleaned_data['image']
			venue.quoteImage = venue_form.cleaned_data['quoteImage']
			venue.save()
			return redirect('venue_list')

		return render(request, template_name, {'form' : venue_form})

	else:
		venue_form = VenueForm()
		return render(request, template_name, {'form' : venue_form})

#CreateView class for creating an enquiry and setting its user and event campaign based on the current user and chosen event
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

#Register view which allows users to create accounts on the platform, then sends them an email
def register(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/index')
	template_html = 'emails/register.html'
	template_text = 'emails/register.txt'
	template_name = 'web_app/register_form.html'
	

	if request.method == 'POST':
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
						subject = 'Registered to Venuebooker'
						from_email = 'Venuebooker <noreply@venuebooker.com>'
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

#User Login View, allows users to login, redirects admins to admin panel
def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/index')
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth_login(request, user)
			if hasattr(user, 'venuebookeruser') or hasattr(user, 'organisationuser') or hasattr(user, 'venueuser') or user.is_superuser:
				return HttpResponseRedirect('/admin')
			else:
				return HttpResponseRedirect('/index')
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

#View for changing user password, then updates session authentication hash so user stays logged in
@login_required(login_url='login')
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

#View for viewing events list and used for searching events with get request parameters
@login_required(login_url='login')
def event_list(request):
	queryset_list = Event_campaign.objects.filter(venue__approved=True)
	typeset = Event_type.objects.all()
	query = request.GET.get("q")
	minCost = request.GET.get("min")
	maxCost = request.GET.get("max")
	minCap = request.GET.get("capmin")
	maxCap = request.GET.get("capmax")
	if query:
		queryset_list = queryset_list.filter(type__name=query)

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
		"type_list": typeset,
		"title": "List",
	}
	return render(request, "eventcampaigns.html", context)

#View for viewing venues list and used for searching venues with get request parameters
@login_required(login_url='login')
def venue_list(request):
	queryset_list = Venue.objects.filter(approved=True)
	query = request.GET.get("q")
	venuetype = request.GET.get("t")
	country_abr = request.GET.get("co")
	if query:
		queryset_list = queryset_list.filter(name__icontains=query)
	if country_abr:
		queryset_list = queryset_list.filter(country=country_abr)
	if venuetype:
		queryset_list = queryset_list.filter(type=venuetype)
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
		"country_list": COUNTRIES,
		"type_list": TYPE_CHOICES,
		"title": "List",
	}
	return render(request, "venues.html", context)


#View class for accepting quotes, sends an email to venues associated with quote
class QuoteAccept(View):
	def post(self, request, pk):
		template_html = 'emails/quote_accepted.html'
		template_text = 'emails/quote_accepted.txt'
		quoteNum = pk
		Quote.objects.filter(pk=quoteNum).update(accepted=True)
		quote = Quote.objects.get(pk=quoteNum)
		try:
			subject = 'Quote Accepted'
			from_email = 'Venuebooker <noreply@venuebooker.com>'
			to = quote.enquiry.event_campaign.venue.organisation.primary_contact.email
			name = quote.enquiry.event_campaign.venue.organisation.primary_contact
			user = quote.enquiry.user.username
			text = get_template(template_text)
			html = get_template(template_html)
			d = {'user': user, 'name': name}
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

#View class for declining quotes, deletes quote from database
class QuoteDecline(View):
	def post(self, request, pk):
		quoteNum = pk
		Quote.objects.filter(pk=quoteNum).delete()
		url = reverse('profile', kwargs={'pk': request.user.id})
		return HttpResponseRedirect(url)
