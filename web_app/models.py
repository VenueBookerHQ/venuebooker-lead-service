from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.contrib.auth.models import Group as Auth_Group
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


from django.contrib.auth.models import BaseUserManager



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


class Contact(models.Model):
    first_name = models.CharField('first name', max_length=30)
    surname = models.CharField('surname', max_length=30)
    telephone = models.CharField('telephone', max_length=15, blank=True)
    mobile = models.CharField('mobile', max_length=15, blank=True)
    email = models.EmailField('email', max_length=50)

    def __str__(self):
        return self.first_name + " " + self.surname

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
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class VenueAdmin(Auth_Group):

    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    def get_users_in_group(self):
        return self.user_set.filter(is_active=1).order_by('first_name', 'last_name')

    def count_users_in_group(self):
        return self.user_set.count()

    def __unicode__(self):
        return self.name

    class Meta:
        permissions = (
             ("access_group_list", "Can access group list"),
             ("access_group", "Can access group"),
        )
        ordering = ["name"]

class VenueUser(Auth_Group):

    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    def get_users_in_group(self):
        return self.user_set.filter(is_active=1).order_by('first_name', 'last_name')

    def count_users_in_group(self):
        return self.user_set.count()

    def __unicode__(self):
        return self.name

    class Meta:
        permissions = (
             ("access_group_list", "Can access group list"),
             ("access_group", "Can access group"),
        )
        ordering = ["name"]

class OrganisationAdmin(Auth_Group):

    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    def get_users_in_group(self):
        return self.user_set.filter(is_active=1).order_by('first_name', 'last_name')

    def count_users_in_group(self):
        return self.user_set.count()

    def __unicode__(self):
        return self.name

    class Meta:
        permissions = (
             ("access_group_list", "Can access group list"),
             ("access_group", "Can access group"),
        )
        ordering = ["name"]
    
class OrganisationUser(Auth_Group):

    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    def get_users_in_group(self):
        return self.user_set.filter(is_active=1).order_by('first_name', 'last_name')

    def count_users_in_group(self):
        return self.user_set.count()

    def __unicode__(self):
        return self.name

    class Meta:
        permissions = (
             ("access_group_list", "Can access group list"),
             ("access_group", "Can access group"),
        )
        ordering = ["name"]

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
    
