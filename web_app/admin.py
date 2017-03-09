from django.contrib import admin

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
from .models import OrganisationAdmin

from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from web_app.models import CustomUser
from web_app.forms import CustomUserChangeForm, CustomUserCreationForm

admin.AdminSite.site_header = "Venuebooker Administration"
admin.AdminSite.site_title = "Venuebooker Site Admin"

admin.site.register(Venue)
admin.site.register(Event_campaign)
admin.site.register(Organisation)
admin.site.register(Enquiry)
admin.site.register(Quote)
admin.site.register(Event_type)
admin.site.register(Contact)
admin.site.register(ContactResponse)
admin.site.register(VenueUser)
admin.site.register(VenueAdmin)
admin.site.register(OrganisationUser)
admin.site.register(OrganisationAdmin)

def roles(self):
    p = sorted([u"<a title='%s'>%s</a>" % (x, x) for x in self.groups.all()])
    if self.user_permissions.count(): p += ['+']
    value = ', '.join(p)
    return mark_safe("<nobr>%s</nobr>" % value)
roles.allow_tags = True
roles.short_description = u'Groups'

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
        ),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('username', 'first_name', 'last_name', roles)
    search_fields = ('username', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
