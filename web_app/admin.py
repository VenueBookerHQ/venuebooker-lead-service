from django.contrib import admin

# Register your models here.
from .models import Venue
from .models import Event_campaign
from .models import Organisation

admin.site.register(Venue)
admin.site.register(Event_campaign)
admin.site.register(Organisation)
admin.site.register(Enquiry)
admin.site.register(Quote)
