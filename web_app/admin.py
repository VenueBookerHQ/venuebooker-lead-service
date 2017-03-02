from django.contrib import admin

# Register your models here.
from .models import Venue
from .models import Event_campaign
from .models import Organisation
from .models import Enquiry
from .models import Quote
from .models import Event_type

from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from web_app.models import CustomUser
from web_app.forms import CustomUserChangeForm, CustomUserCreationForm

admin.site.register(Venue)
admin.site.register(Event_campaign)
admin.site.register(Organisation)
admin.site.register(Enquiry)
admin.site.register(Quote)
admin.site.register(Event_type)

class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference the removed 'username' field
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
    list_display = ('username', 'first_name', 'last_name')
    search_fields = ('username', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
