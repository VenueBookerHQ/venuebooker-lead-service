from django.contrib.auth.models import User
from web_app.models import ContactResponse
from web_app.models import Organisation, Venue, Event_campaign, Enquiry, Quote, Contact, OrganisationUser, VenueUser
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from web_app.models import CustomUser

#UserForm which is used by the registration page to allow users to register an account
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

#ProfileForm which is used by the update details page to allow users to edit their account
class ProfileForm(forms.ModelForm):	
	class Meta:
		model = CustomUser
		fields = ['avatar']

#Extension of the Django base user form, used for creation of users
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


#Extension of the Django base user change form, used for changing of user details
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

#Contact Form, used for the contact details of users
class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['first_name', 'last_name', 'email', 'telephone', 'mobile', 'company']

#Contact Response Form, used for the submission of contact us requests
class ContactResponseForm(forms.ModelForm):
	class Meta:
		model = ContactResponse
		fields = ['name', 'email', 'phone', 'message']

#Organisation Form, used for creation of Organisations
class OrganisationForm(forms.ModelForm):
	class Meta:
		model = Organisation
		fields = ['name', 'image', 'address', 'primary_contact', 'description']

#Venue Form, used for creation of Venues in the venue signup process
class VenueForm(forms.ModelForm):
	class Meta:
		model = Venue
		fields = ['name', 'type', 'image', 'address', 'city', 'country', 'quoteImage', 'facebook_link', 'twitter_link', 'instagram_link', 'description', 'organisation']

#Event Campaign Form, used for creation of Event Campaigns
class EventCampaignForm(forms.ModelForm):
	class Meta:
		model = Event_campaign
		fields = ['name', 'type', 'details', 'startTime', 'endTime', 'recurring', 'image', 'capacity', 'cost_per_capacity_unit', 'venue']

#Enquiry Form, used for submission of Enquiries
class EnquiryForm(forms.ModelForm):
	class Meta:
		model = Enquiry
		fields = ['message', 'attendeeNum', 'date', 'event_campaign', 'user', 'approved']

#Quote Form, used for creation of Quotes
class QuoteForm(forms.ModelForm):
	class Meta:
		model = Quote
		fields = ['description', 'cost', 'accepted', 'enquiry']

#Organisation User Form, used for creation of Organisation Users
class OrganisationUserForm(forms.ModelForm):
	class Meta:
		model = OrganisationUser
		fields = ['user','position','organisation']

#Venue User Form, used for creation of Venue Users
class VenueUserForm(forms.ModelForm):
	class Meta:
		model = VenueUser
		fields = ['user','position','venue']

