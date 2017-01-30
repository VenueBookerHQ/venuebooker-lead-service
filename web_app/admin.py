from django.contrib import admin

# Register your models here.
from .models import Venue
from .models import Event_campaign

admin.site.register(Venue)
admin.site.register(Event_campaign)
