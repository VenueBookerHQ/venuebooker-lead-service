from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User




class Organisation(models.Model):
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=200)

    def get_absolute_url(self):
	    return reverse('organisation_detail', kwargs={'pk': self.pk})


    def __str__(self):              
        return self.name

class Venue(models.Model):
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=200)
    socialmedialinks = ArrayField(models.TextField(max_length=200, blank=True))
    description = models.TextField(max_length=200)
    image = models.FileField()
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    def get_absolute_url(self):
    	return reverse('venue_detail', kwargs={'pk': self.pk})
	

    def __str__(self):              
        return self.name


class Event_type(models.Model):
    name = models.TextField(max_length=40)
    description = models.TextField(max_length=500)
    active = models.BooleanField()
    seasonal = models.BooleanField()

    def __str__(self):              
        return self.name

class Event_campaign(models.Model):
    type = models.ForeignKey(Event_type, on_delete=models.CASCADE)
    details = models.TextField(max_length=200)
    name = models.TextField(max_length=200)
    startTime = models.TimeField(blank=True)
    endTime = models.TimeField(blank=True)
    recurring = models.BooleanField()
    image = models.FileField()
    capacity = models.IntegerField()
    cost_per_capacity_unit = models.FloatField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    def get_absolute_url(self):
	    return reverse('event_campaign_detail', kwargs={'pk': self.pk})


    def __str__(self):              
        return self.name

class Enquiry(models.Model):
    message = models.TextField()
    attendeeNum = models.IntegerField()
    date = models.DateField()
    event_campaign = models.ForeignKey(Event_campaign, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
	    return reverse('index')
    def __str__(self):              
        return self.name

class Quote(models.Model):
    description = models.TextField()
    cost = models.FloatField()
    accepted = models.BooleanField()
    enquiry = models.ForeignKey(Enquiry, on_delete=models.CASCADE)

    def get_absolute_url(self):
	    return reverse('index')
    def __str__(self):              
        return self.name
    
