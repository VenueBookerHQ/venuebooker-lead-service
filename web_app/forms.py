from django.contrib.auth.models import User
from web_app.models import ContactResponse
from web_app.models import Organisation, Venue, Event_campaign, Enquiry, Quote, Contact, OrganisationUser, VenueUser
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from web_app.models import CustomUser


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	password_confirm = forms.CharField(widget=forms.PasswordInput)
	
	class Meta:
		model = CustomUser
		fields = ['username', 'avatar', 'password', 'password_confirm']
	
	def clean(self):
		clean_data = super(UserForm, self).clean()

		password = clean_data.get('password')
		password_confirm = clean_data.get('password_confirm')

		if password and password_confirm:
			if password != password_confirm:
				msg = "The passwords do not match."
				self.add_error('password_confirm', msg)
				raise forms.ValidationError("The passwords do not match.")
		return clean_data

class ProfileForm(forms.ModelForm):	
	class Meta:
		model = CustomUser
		fields = ['avatar']

class CustomUserCreationForm(UserCreationForm):
	"""
	A form that creates a user, with no privileges, from the given email and
	password.
	"""

	def __init__(self, *args, **kargs):
		super(CustomUserCreationForm, self).__init__(*args, **kargs)

	class Meta:
		model = CustomUser
		fields = ("username","email")


class CustomUserChangeForm(UserChangeForm):
	"""A form for updating users. Includes all the fields on
	the user, but replaces the password field with admin's
	password hash display field.
	"""

	def __init__(self, *args, **kargs):
		super(CustomUserChangeForm, self).__init__(*args, **kargs)

	class Meta:
		model = CustomUser
		fields = ("username","email")

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['first_name', 'last_name', 'email', 'telephone', 'mobile', 'company']

class ContactResponseForm(forms.ModelForm):
	class Meta:
		model = ContactResponse
		fields = ['name', 'email', 'phone', 'message']

class OrganisationForm(forms.ModelForm):
	class Meta:
		model = Organisation
		fields = ['name', 'image', 'address', 'primary_contact', 'description']

class VenueForm(forms.ModelForm):
	class Meta:
		model = Venue
		fields = ['name', 'type', 'image', 'address', 'city', 'country', 'quoteImage', 'facebook_link', 'twitter_link', 'instagram_link', 'description', 'organisation']

class EventCampaignForm(forms.ModelForm):
	class Meta:
		model = Event_campaign
		fields = ['name', 'type', 'details', 'startTime', 'endTime', 'recurring', 'image', 'capacity', 'cost_per_capacity_unit', 'venue']

class EnquiryForm(forms.ModelForm):
	class Meta:
		model = Enquiry
		fields = ['message', 'attendeeNum', 'date', 'event_campaign', 'user', 'approved']

class QuoteForm(forms.ModelForm):
	class Meta:
		model = Quote
		fields = ['description', 'cost', 'accepted', 'enquiry']

class OrganisationUserForm(forms.ModelForm):
	class Meta:
		model = OrganisationUser
		fields = ['user','position','organisation']

class VenueUserForm(forms.ModelForm):
	class Meta:
		model = VenueUser
		fields = ['user','position','venue']

