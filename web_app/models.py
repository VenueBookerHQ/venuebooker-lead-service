from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.contrib.auth.models import Group as Auth_Group
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html
import datetime
from django.utils import timezone


from django.contrib.auth.models import BaseUserManager


class Contact(models.Model):
    first_name = models.CharField('first name', max_length=30)
    surname = models.CharField('surname', max_length=30)
    telephone = models.CharField('telephone', max_length=15, blank=True)
    mobile = models.CharField('mobile', max_length=15, blank=True)
    email = models.EmailField('email', max_length=50)

    def __str__(self):
        return self.first_name + " " + self.surname

class Organisation(models.Model):
    name = models.TextField(max_length=200)
    image = models.ImageField(blank=True, default='default.jpg')
    address = models.TextField(max_length=200)
    primary_contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    description = models.TextField('description')

    def get_absolute_url(self):
	    return reverse('organisation_detail', kwargs={'pk': self.pk})


    def __str__(self):              
        return str(self.id) + " " + self.name

    def image_preview_large(self):
        if self.image:
            return format_html(
                '<img src="{}" width="150" height="150"/>',
                self.image.url
            )
        return 'No Logo'

    image_preview_large.short_description = 'Image Preview'

    def image_preview_small(self):
        if self.image:
            return format_html(
                '<img src="{}" width="50" height="50"/>',
                self.image.url
            )
        return 'No Logo'

    image_preview_small.short_description = 'Image Preview'

class Venue(models.Model):
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=200)
    facebook_link = models.TextField(max_length=200, blank=True)
    twitter_link = models.TextField(max_length=200, blank=True)
    instagram_link = models.TextField(max_length=200, blank=True)
    description = models.TextField(max_length=200)
    image = models.ImageField(blank=True, default='default.jpg')
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

class CustomUserManager(BaseUserManager):

    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, True,
                                 **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField('email', max_length=50)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True)
    date_joined = models.DateTimeField(_('date joined'), default=datetime.datetime.now())
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name


class VenueAdmin(models.Model):
    user = models.OneToOneField(CustomUser, verbose_name="User account details")
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    def __str__(self):
        return self.organisation.name + " Venue Admin " + str(self.user.username)

class VenueUser(models.Model):
    user = models.OneToOneField(CustomUser, verbose_name="User account details")
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    def __str__(self):
        return self.organisation.name + " Venue User " + str(self.user.username)

class OrganisationAdmin(models.Model):
    user = models.OneToOneField(CustomUser, verbose_name="User account details")
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    def __str__(self):
        return self.organisation.name + " Organisation User " + str(self.user.username)
    
class OrganisationUser(models.Model):
    user = models.OneToOneField(CustomUser, verbose_name="User account details")
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    def __str__(self):
        return self.organisation.name + " Organisation Admin " + str(self.user.username)

class Enquiry(models.Model):
    message = models.TextField()
    attendeeNum = models.IntegerField()
    date = models.DateField()
    event_campaign = models.ForeignKey(Event_campaign, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

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

class ContactResponse(models.Model):
    name = models.CharField('name', max_length=300)
    email = models.EmailField('email', max_length=50)
    phone = models.CharField('phone number', max_length=15, blank=True)
    message = models.TextField('message')
    timestamp = models.DateTimeField('timestamp', auto_now_add=True)

    def __str__(self):
        return str(self.id) + " " + self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
