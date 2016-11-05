from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Venue(models.Model):
    priority = models.IntegerField()
    type = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    places = models.IntegerField()
    image = models.CharField(max_length=100)

    def __str__(self):              # __unicode__ on Python 2
        return self.type
