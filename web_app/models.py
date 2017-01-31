from django.db import models

class Venue(models.Model):
    name = models.TextField(max_length=200)
    type = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    image = models.FileField()

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
