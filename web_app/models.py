from django.db import models
from django.core.urlresolvers import reverse

class Venue(models.Model):
    name = models.TextField(max_length=200)
    type = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    image = models.FileField()

    def get_absolute_url(self):
	return reverse('detail', kwargs={'pk': self.pk})
	

    def __str__(self):              # __unicode__ on Python 2
        return self.type


class Event_campaign(models.Model):
    type = models.CharField(max_length=30)
    details = models.TextField(max_length=200)
    name = models.TextField(max_length=200)
    image = models.FileField()
    capacity = models.IntegerField()

    def __str__(self):              # __unicode__ on Python 2
        return self.type
