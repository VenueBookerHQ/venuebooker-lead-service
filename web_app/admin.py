from django.contrib import admin
from django.db.models import Q

# Register your models here.
from .models import Venue
from .models import Event_campaign
from .models import Organisation
from .models import Enquiry
from .models import Quote
from .models import Event_type
from .models import Contact
from .models import ContactResponse
from .models import VenueUser
from .models import OrganisationUser
from .models import VenuebookerUser
from .models import EventImage
from .models import VenueImage
from .models import Lead


from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from web_app.models import CustomUser
from web_app.forms import CustomUserChangeForm, CustomUserCreationForm, OrganisationForm, VenueForm, EventCampaignForm, EnquiryForm, QuoteForm, OrganisationUserForm, VenueUserForm, ContactForm

admin.AdminSite.site_header = "Venuebooker Administration"
admin.AdminSite.site_title = "Venuebooker Site Admin"
admin.AdminSite.site_title = "Site Administration"

admin.site.register(Event_type)
admin.site.register(ContactResponse)
admin.site.register(VenuebookerUser)

class EventImageInline(admin.StackedInline):
	model = EventImage
	max_num = 10
	extra = 0

class VenueImageInline(admin.StackedInline):
	model = VenueImage
	max_num = 10
	extra = 0

class OrganisationUserInline(admin.StackedInline):
	model = OrganisationUser
	extra = 1

class VenueUserInline(admin.StackedInline):
	model = VenueUser
	extra = 1


class OrganisationAdmin(admin.ModelAdmin):
	form = OrganisationForm
	fieldsets = (
		('Basic Details', {
			'fields': ('name', ('image', 'image_preview_large'), 'address', 'description', 'primary_contact')
		}),
	)

	list_display = ('image_preview_small', 'name', 'address', 'primary_contact',
					 'associated_user_accounts')
	list_display_links = ('image_preview_small', 'name')
	inlines = [OrganisationUserInline]
	readonly_fields = ('image_preview_large',)
	search_fields = ['name']
	
	def get_queryset(self, request):
		if request.user.is_superuser or hasattr(request.user, 'venuebookeruser'):
			return Organisation.objects.all()
		return Organisation.objects.filter(name=request.user.organisationuser.organisation)

	
class VenueAdmin(admin.ModelAdmin):
	form = VenueForm
	user_fields = ['name', 'type', 'image','address', 'city', 'country', 'quoteImage','facebook_link','twitter_link','instagram_link','description','organisation']
	admin_fields = ['approved']
	def get_form(self, request, obj=None, **kwargs):
		if request.user.is_superuser or hasattr(request.user, 'venuebookeruser'):
			self.fields = self.user_fields + self.admin_fields
		else:
			self.fields = self.user_fields
		return super(VenueAdmin, self).get_form(request, obj, **kwargs)

	list_display = ('image_preview_small', 'name', 'type', 'address', 'organisation')
	list_display_links = ('image_preview_small', 'name')
	inlines = [VenueUserInline, VenueImageInline]
	readonly_fields = ('image_preview_large',)
	search_fields = ['name']

	def save_model(self, request, obj, form, change):
		if not obj.organisation:
			obj.organisation = request.user.organisationuser.organisation
		super(VenueAdmin, self).save_model(request, obj, form, change)
	
	def get_queryset(self, request):
		if request.user.is_superuser or hasattr(request.user, 'venuebookeruser'):
			return Venue.objects.all()
		elif hasattr(request.user, 'venueuser'):
			return Venue.objects.filter(name=request.user.venueuser.venue)
		return Venue.objects.filter(organisation=request.user.organisationuser.organisation)

class EventCampaignAdmin(admin.ModelAdmin):
	form = EventCampaignForm
	fieldsets = (
		('Basic Details', {
			'fields': ('name', ('image', 'image_preview_large'), 'type', 'details', 'startTime', 'endTime', 'recurring', 'capacity', 'cost_per_capacity_unit', 'venue')
		}),
	)

	list_display = ('image_preview_small', 'name', 'type', 'venue')
	list_display_links = ('image_preview_small', 'name')
	readonly_fields = ('image_preview_large',)
	search_fields = ['name']
	inlines = [EventImageInline]
	
	def get_form(self, request, obj=None, **kwargs):
		form = super(EventCampaignAdmin, self).get_form(request, obj, **kwargs)
		if hasattr(request.user, 'organisationuser'):
			form.base_fields['venue'].queryset = Venue.objects.filter(organisation=request.user.organisationuser.organisation)
		elif hasattr(request.user, 'venueuser'):
			form.base_fields['venue'].queryset = Venue.objects.filter(name=request.user.venueuser.venue)
		else:
			form.base_fields['venue'].queryset = Venue.objects.all()
		return form

	def get_queryset(self, request):
		if request.user.is_superuser or hasattr(request.user, 'venuebookeruser'):
			return Event_campaign.objects.all()
		elif hasattr(request.user, 'organisationuser'):
			return Event_campaign.objects.filter(venue__organisation=request.user.organisationuser.organisation)
		return Event_campaign.objects.filter(venue=request.user.venueuser.venue)

class EnquiryAdmin(admin.ModelAdmin):
	form = EnquiryForm
	fieldsets = (
		('Basic Details', {
			'fields': ('message', 'attendeeNum', 'date', 'event_campaign', 'user', 'approved')
		}),
	)

	list_display = ('user', 'event_campaign', 'date', 'approved')
	list_display_links = ('user',)
	search_fields = ['user']
	
	def get_queryset(self, request):
		if request.user.is_superuser or hasattr(request.user, 'venuebookeruser'):
			return Enquiry.objects.all()
		elif hasattr(request.user, 'organisationuser'):
			return Enquiry.objects.filter(event_campaign__venue__organisation=request.user.organisationuser.organisation, approved=True)
		return Enquiry.objects.filter(event_campaign__venue=request.user.venueuser.venue, approved=True)

class QuoteAdmin(admin.ModelAdmin):
	form = QuoteForm
	fieldsets = (
		('Basic Details', {
			'fields': ('description', 'cost', 'accepted', 'enquiry')
		}),
	)

	list_display = ('enquiry', 'cost', 'accepted')
	list_display_links = ('enquiry',)
	search_fields = ['enquiry']
	readonly_fields = ('accepted',)

	def get_form(self, request, obj=None, **kwargs):
		form = super(QuoteAdmin, self).get_form(request, obj, **kwargs)
		if hasattr(request.user, 'organisationuser'):
			form.base_fields['enquiry'].queryset = Enquiry.objects.filter(event_campaign__venue__organisation=request.user.organisationuser.organisation, approved=True)
		elif hasattr(request.user, 'venueuser'):
			form.base_fields['enquiry'].queryset = Enquiry.objects.filter(event_campaign__venue=request.user.venueuser.venue, approved=True)
		else:
			form.base_fields['enquiry'].queryset = Enquiry.objects.all()
		return form
	
	def get_queryset(self, request):
		if request.user.is_superuser or hasattr(request.user, 'venuebookeruser'):
			return Quote.objects.all()
		elif hasattr(request.user, 'organisationuser'):
			return Quote.objects.filter(enquiry__event_campaign__venue__organisation=request.user.organisationuser.organisation, enquiry__approved=True)
		return Quote.objects.filter(enquiry__event_campaign__venue=request.user.venueuser.venue, enquiry__approved=True)

class CustomUserAdmin(UserAdmin):
	fieldsets = (
		(None, {'fields': ('username', 'email', 'avatar', 'contact', 'password')}),
		(_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
									   'groups', 'user_permissions')}),
		(_('Important dates'), {'fields': ('last_login',)}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('username', 'email', 'avatar', 'password1', 'password2')}
		),
	)
	form = CustomUserChangeForm
	add_form = CustomUserCreationForm
	list_display = ('username',)
	search_fields = ('username',)
	ordering = ('username',)
	
	def get_queryset(self, request):
		if request.user.is_superuser or hasattr(request.user, 'venuebookeruser'):
			return CustomUser.objects.all()
		elif hasattr(request.user, 'organisationuser'):
			return CustomUser.objects.filter(Q(organisationuser__organisation=request.user.organisationuser.organisation) | Q(venueuser__venue__organisation=request.user.organisationuser.organisation))
		return CustomUser.objects.filter(venueuser__venue=request.user.venueuser.venue)

class VenueUserAdmin(admin.ModelAdmin):
	form = VenueUserForm
	user_fields = ['user','position','venue']


	list_display = ('user', 'position', 'venue')
	list_display_links = ('user',)
	search_fields = ['user']

	
	def get_queryset(self, request):
		if request.user.is_superuser or hasattr(request.user, 'venuebookeruser'):
			return VenueUser.objects.all()
		elif hasattr(request.user, 'venueuser'):
			return VenueUser.objects.filter(venue=request.user.venueuser.venue)
		return VenueUser.objects.filter(venue__organisation=request.user.organisationuser.organisation)

class OrganisationUserAdmin(admin.ModelAdmin):
	form = OrganisationUserForm
	user_fields = ['user','position','organisation']


	list_display = ('user', 'position', 'organisation')
	list_display_links = ('user',)
	search_fields = ['user']

	
	def get_queryset(self, request):
		if request.user.is_superuser or hasattr(request.user, 'venuebookeruser'):
			return OrganisationUser.objects.all()
		else:
			return OrganisationUser.objects.filter(organisation=request.user.organisationuser.organisation)

class ContactAdmin(admin.ModelAdmin):
	form = ContactForm
	user_fields = ['first_name', 'last_name', 'email', 'telephone', 'mobile', 'company']
	list_display = ('first_name', 'last_name', 'email', 'telephone', 'mobile', 'company')
	list_display_links = ('first_name', 'last_name')
	search_fields = ['first_name', 'last_name', 'email', 'company']

admin.site.register(Lead)
admin.site.register(EventImage)
admin.site.register(VenueImage)
admin.site.register(Contact, ContactAdmin)
admin.site.register(VenueUser, VenueUserAdmin)
admin.site.register(OrganisationUser, OrganisationUserAdmin)
admin.site.register(Enquiry, EnquiryAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Event_campaign, EventCampaignAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
