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
from .models import VenueAdmin
from .models import OrganisationUser


from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from web_app.models import CustomUser
from web_app.forms import CustomUserChangeForm, CustomUserCreationForm, OrganisationForm, VenueForm

admin.AdminSite.site_header = "Venuebooker Administration"
admin.AdminSite.site_title = "Venuebooker Site Admin"

admin.site.register(Event_campaign)
admin.site.register(Enquiry)
admin.site.register(Quote)
admin.site.register(Event_type)
admin.site.register(Contact)
admin.site.register(ContactResponse)
admin.site.register(VenueUser)
admin.site.register(OrganisationUser)

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
        qs = super(OrganisationAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(name=request.user.organisationuser.organisation)

class VenueAdmin(admin.ModelAdmin):
    form = VenueForm
    fieldsets = (
        ('Basic Details', {
            'fields': ('name', ('image', 'image_preview_large'), 'address', 'facebook_link', 'twitter_link', 'instagram_link', 'description')
        }),
    )

    list_display = ('image_preview_small', 'name', 'address', 'organisation')
    list_display_links = ('image_preview_small', 'name')
    inlines = [VenueUserInline]
    readonly_fields = ('image_preview_large',)
    search_fields = ['name']
    
    def get_queryset(self, request):
        qs = super(VenueAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif request.user.organisationuser__isnull=True:
            return qs.filter(name=request.user.venueuser.venue)
        return qs.filter(organisation=request.user.organisationuser.organisation)

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
        ),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('username', 'first_name', 'last_name')
    search_fields = ('username', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(Venue, VenueAdmin)
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
