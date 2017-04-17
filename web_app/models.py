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
from datetime import datetime
from django.utils import timezone
from django.template import *
from django.template.loader import get_template
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import BaseUserManager

## Country Codes and CountryField https://djangosnippets.org/snippets/1476/ author username: dougal
COUNTRIES = (
	('GB', _('United Kingdom')), 
	('AF', _('Afghanistan')), 
	('AX', _('Aland Islands')), 
	('AL', _('Albania')), 
	('DZ', _('Algeria')), 
	('AS', _('American Samoa')), 
	('AD', _('Andorra')), 
	('AO', _('Angola')), 
	('AI', _('Anguilla')), 
	('AQ', _('Antarctica')), 
	('AG', _('Antigua and Barbuda')), 
	('AR', _('Argentina')), 
	('AM', _('Armenia')), 
	('AW', _('Aruba')), 
	('AU', _('Australia')), 
	('AT', _('Austria')), 
	('AZ', _('Azerbaijan')), 
	('BS', _('Bahamas')), 
	('BH', _('Bahrain')), 
	('BD', _('Bangladesh')), 
	('BB', _('Barbados')), 
	('BY', _('Belarus')), 
	('BE', _('Belgium')), 
	('BZ', _('Belize')), 
	('BJ', _('Benin')), 
	('BM', _('Bermuda')), 
	('BT', _('Bhutan')), 
	('BO', _('Bolivia')), 
	('BA', _('Bosnia and Herzegovina')), 
	('BW', _('Botswana')), 
	('BV', _('Bouvet Island')), 
	('BR', _('Brazil')), 
	('IO', _('British Indian Ocean Territory')), 
	('BN', _('Brunei Darussalam')), 
	('BG', _('Bulgaria')), 
	('BF', _('Burkina Faso')), 
	('BI', _('Burundi')), 
	('KH', _('Cambodia')), 
	('CM', _('Cameroon')), 
	('CA', _('Canada')), 
	('CV', _('Cape Verde')), 
	('KY', _('Cayman Islands')), 
	('CF', _('Central African Republic')), 
	('TD', _('Chad')), 
	('CL', _('Chile')), 
	('CN', _('China')), 
	('CX', _('Christmas Island')), 
	('CC', _('Cocos (Keeling) Islands')), 
	('CO', _('Colombia')), 
	('KM', _('Comoros')), 
	('CG', _('Congo')), 
	('CD', _('Congo, The Democratic Republic of the')), 
	('CK', _('Cook Islands')), 
	('CR', _('Costa Rica')), 
	('CI', _('Cote d\'Ivoire')), 
	('HR', _('Croatia')), 
	('CU', _('Cuba')), 
	('CY', _('Cyprus')), 
	('CZ', _('Czech Republic')), 
	('DK', _('Denmark')), 
	('DJ', _('Djibouti')), 
	('DM', _('Dominica')), 
	('DO', _('Dominican Republic')), 
	('EC', _('Ecuador')), 
	('EG', _('Egypt')), 
	('SV', _('El Salvador')), 
	('GQ', _('Equatorial Guinea')), 
	('ER', _('Eritrea')), 
	('EE', _('Estonia')), 
	('ET', _('Ethiopia')), 
	('FK', _('Falkland Islands (Malvinas)')), 
	('FO', _('Faroe Islands')), 
	('FJ', _('Fiji')), 
	('FI', _('Finland')), 
	('FR', _('France')), 
	('GF', _('French Guiana')), 
	('PF', _('French Polynesia')), 
	('TF', _('French Southern Territories')), 
	('GA', _('Gabon')), 
	('GM', _('Gambia')), 
	('GE', _('Georgia')), 
	('DE', _('Germany')), 
	('GH', _('Ghana')), 
	('GI', _('Gibraltar')), 
	('GR', _('Greece')), 
	('GL', _('Greenland')), 
	('GD', _('Grenada')), 
	('GP', _('Guadeloupe')), 
	('GU', _('Guam')), 
	('GT', _('Guatemala')), 
	('GG', _('Guernsey')), 
	('GN', _('Guinea')), 
	('GW', _('Guinea-Bissau')), 
	('GY', _('Guyana')), 
	('HT', _('Haiti')), 
	('HM', _('Heard Island and McDonald Islands')), 
	('VA', _('Holy See (Vatican City State)')), 
	('HN', _('Honduras')), 
	('HK', _('Hong Kong')), 
	('HU', _('Hungary')), 
	('IS', _('Iceland')), 
	('IN', _('India')), 
	('ID', _('Indonesia')), 
	('IR', _('Iran, Islamic Republic of')), 
	('IQ', _('Iraq')), 
	('IE', _('Ireland')), 
	('IM', _('Isle of Man')), 
	('IL', _('Israel')), 
	('IT', _('Italy')), 
	('JM', _('Jamaica')), 
	('JP', _('Japan')), 
	('JE', _('Jersey')), 
	('JO', _('Jordan')), 
	('KZ', _('Kazakhstan')), 
	('KE', _('Kenya')), 
	('KI', _('Kiribati')), 
	('KP', _('Korea, Democratic People\'s Republic of')), 
	('KR', _('Korea, Republic of')), 
	('KW', _('Kuwait')), 
	('KG', _('Kyrgyzstan')), 
	('LA', _('Lao People\'s Democratic Republic')), 
	('LV', _('Latvia')), 
	('LB', _('Lebanon')), 
	('LS', _('Lesotho')), 
	('LR', _('Liberia')), 
	('LY', _('Libyan Arab Jamahiriya')), 
	('LI', _('Liechtenstein')), 
	('LT', _('Lithuania')), 
	('LU', _('Luxembourg')), 
	('MO', _('Macao')), 
	('MK', _('Macedonia, The Former Yugoslav Republic of')), 
	('MG', _('Madagascar')), 
	('MW', _('Malawi')), 
	('MY', _('Malaysia')), 
	('MV', _('Maldives')), 
	('ML', _('Mali')), 
	('MT', _('Malta')), 
	('MH', _('Marshall Islands')), 
	('MQ', _('Martinique')), 
	('MR', _('Mauritania')), 
	('MU', _('Mauritius')), 
	('YT', _('Mayotte')), 
	('MX', _('Mexico')), 
	('FM', _('Micronesia, Federated States of')), 
	('MD', _('Moldova')), 
	('MC', _('Monaco')), 
	('MN', _('Mongolia')), 
	('ME', _('Montenegro')), 
	('MS', _('Montserrat')), 
	('MA', _('Morocco')), 
	('MZ', _('Mozambique')), 
	('MM', _('Myanmar')), 
	('NA', _('Namibia')), 
	('NR', _('Nauru')), 
	('NP', _('Nepal')), 
	('NL', _('Netherlands')), 
	('AN', _('Netherlands Antilles')), 
	('NC', _('New Caledonia')), 
	('NZ', _('New Zealand')), 
	('NI', _('Nicaragua')), 
	('NE', _('Niger')), 
	('NG', _('Nigeria')), 
	('NU', _('Niue')), 
	('NF', _('Norfolk Island')), 
	('MP', _('Northern Mariana Islands')), 
	('NO', _('Norway')), 
	('OM', _('Oman')), 
	('PK', _('Pakistan')), 
	('PW', _('Palau')), 
	('PS', _('Palestinian Territory, Occupied')), 
	('PA', _('Panama')), 
	('PG', _('Papua New Guinea')), 
	('PY', _('Paraguay')), 
	('PE', _('Peru')), 
	('PH', _('Philippines')), 
	('PN', _('Pitcairn')), 
	('PL', _('Poland')), 
	('PT', _('Portugal')), 
	('PR', _('Puerto Rico')), 
	('QA', _('Qatar')), 
	('RE', _('Reunion')), 
	('RO', _('Romania')), 
	('RU', _('Russian Federation')), 
	('RW', _('Rwanda')), 
	('BL', _('Saint Barthelemy')), 
	('SH', _('Saint Helena')), 
	('KN', _('Saint Kitts and Nevis')), 
	('LC', _('Saint Lucia')), 
	('MF', _('Saint Martin')), 
	('PM', _('Saint Pierre and Miquelon')), 
	('VC', _('Saint Vincent and the Grenadines')), 
	('WS', _('Samoa')), 
	('SM', _('San Marino')), 
	('ST', _('Sao Tome and Principe')), 
	('SA', _('Saudi Arabia')), 
	('SN', _('Senegal')), 
	('RS', _('Serbia')), 
	('SC', _('Seychelles')), 
	('SL', _('Sierra Leone')), 
	('SG', _('Singapore')), 
	('SK', _('Slovakia')), 
	('SI', _('Slovenia')), 
	('SB', _('Solomon Islands')), 
	('SO', _('Somalia')), 
	('ZA', _('South Africa')), 
	('GS', _('South Georgia and the South Sandwich Islands')), 
	('ES', _('Spain')), 
	('LK', _('Sri Lanka')), 
	('SD', _('Sudan')), 
	('SR', _('Suriname')), 
	('SJ', _('Svalbard and Jan Mayen')), 
	('SZ', _('Swaziland')), 
	('SE', _('Sweden')), 
	('CH', _('Switzerland')), 
	('SY', _('Syrian Arab Republic')), 
	('TW', _('Taiwan, Province of China')), 
	('TJ', _('Tajikistan')), 
	('TZ', _('Tanzania, United Republic of')), 
	('TH', _('Thailand')), 
	('TL', _('Timor-Leste')), 
	('TG', _('Togo')), 
	('TK', _('Tokelau')), 
	('TO', _('Tonga')), 
	('TT', _('Trinidad and Tobago')), 
	('TN', _('Tunisia')), 
	('TR', _('Turkey')), 
	('TM', _('Turkmenistan')), 
	('TC', _('Turks and Caicos Islands')), 
	('TV', _('Tuvalu')), 
	('UG', _('Uganda')), 
	('UA', _('Ukraine')), 
	('AE', _('United Arab Emirates')), 
	('US', _('United States')), 
	('UM', _('United States Minor Outlying Islands')), 
	('UY', _('Uruguay')), 
	('UZ', _('Uzbekistan')), 
	('VU', _('Vanuatu')), 
	('VE', _('Venezuela')), 
	('VN', _('Viet Nam')), 
	('VG', _('Virgin Islands, British')), 
	('VI', _('Virgin Islands, U.S.')), 
	('WF', _('Wallis and Futuna')), 
	('EH', _('Western Sahara')), 
	('YE', _('Yemen')), 
	('ZM', _('Zambia')), 
	('ZW', _('Zimbabwe')), 
)

TYPE_CHOICES = (
		('BAR', 'Bar'),
		('RESTAURANT', 'Restaurant'),
		('HOTEL', 'Hotel'),
		('CONFERENCE', 'Conference Center'),
		('GALLERY', 'Gallery'),
		('WAREHOUSE', 'Warehouse'),
		('OUTSIDE', 'Outside'),
		('ROOFTOP', 'Rooftop'),
		('PRIVATE', 'Private Venue'),
		('OTHER', 'Other')
	)
class CountryField(models.CharField):
	
	def __init__(self, *args, **kwargs):
		kwargs.setdefault('max_length', 2)
		kwargs.setdefault('choices', COUNTRIES)

		super(CountryField, self).__init__(*args, **kwargs)

	def get_internal_type(self):
		return "CharField"

class Contact(models.Model):
	first_name = models.CharField('first name', max_length=30)
	last_name = models.CharField('last name', max_length=30)
	telephone = models.CharField('telephone', max_length=15, blank=True)
	mobile = models.CharField('mobile', max_length=15, blank=True)
	email = models.EmailField('email', max_length=50)
	company = models.CharField('company (optional)', max_length=50, blank=True)

	def __str__(self):
		return self.first_name + " " + self.last_name

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
	is_staff = models.BooleanField(_('staff status'), default=False,
		help_text=_('Designates whether the user can log into this admin '
					'site.'))
	is_active = models.BooleanField(_('active'), default=True,
		help_text=_('Designates whether this user should be treated as '
					'active. Unselect this instead of deleting accounts.'))
	date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
	is_active = models.BooleanField(_('active'), default=True)
	avatar = models.ImageField(null=True, blank=True)
	contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True)

	objects = CustomUserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')

	def get_full_name(self):
		"""
		Returns the username and email, with a space in between.
		"""
		full_name = '%s %s' % (self.username, self.email)
		return full_name.strip()

	def get_short_name(self):
		"Returns the short name for the user."
		return self.username

	class Meta:
		verbose_name = 'User Account'
		verbose_name_plural = 'My User Accounts'

@receiver(post_save, sender=CustomUser)
def social_auth_contact_email(sender, **kwargs):
	user = kwargs.get('instance')
	if user.is_authenticated:
		if user.contact:
			return
		else:
			if user.social_auth.filter(provider='google-oauth2'):
				social = user.social_auth.get(provider='google-oauth2')
			elif user.social_auth.filter(provider='facebook'):
				social = user.social_auth.get(provider='facebook')
				fname = social.extra_data['first_name']
				lname = social.extra_data['last_name']
				emailAddress = social.extra_data['email']
				contact, created = Contact.objects.get_or_create(first_name=fname, last_name=lname, email=emailAddress,)
				if created:
					user.contact = contact
					user.save()
			elif user.social_auth.filter(provider='twitter'):
				social = user.social_auth.get(provider='twitter')
			elif user.social_auth.filter(provider='linkedin-oauth2'):
				social = user.social_auth.get(provider='linkedin-oauth2')
				fname = social.extra_data['first_name']
				lname = social.extra_data['last_name']
				emailAddress = social.extra_data['email_address']
				contact, created = Contact.objects.get_or_create(first_name=fname, last_name=lname, email=emailAddress,)
				if created:
					user.contact = contact
					user.save()
			else:
				return


class Organisation(models.Model):
	name = models.CharField(max_length=50)
	image = models.ImageField(blank=True, default='default.jpg')
	address = models.CharField(max_length=150)
	primary_contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
	description = models.TextField('description')

	def get_absolute_url(self):
		return reverse('organisation_detail', kwargs={'pk': self.pk})


	def __str__(self):			  
		return self.name

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

	def associated_user_accounts(self):
		if not self.organisationuser_set.count():
			return 'No Accounts'
		return ','.join(str(item.user.id) + ': ' + item.user.username for item in self.organisationuser_set.all())

	associated_user_accounts.short_description = 'User Accounts'

	class Meta:
		verbose_name = 'Organisation'
		verbose_name_plural = 'My Organisations'	

class Venue(models.Model):
	name = models.CharField(max_length=50)
	type = models.CharField(max_length=20, choices=TYPE_CHOICES)
	address = models.CharField(max_length=150)
	city = models.CharField(max_length=50)
	country = CountryField(blank=True)
	facebook_link = models.URLField(max_length=255, blank=True)
	twitter_link = models.URLField(max_length=255, blank=True)
	instagram_link = models.URLField(max_length=255, blank=True)
	description = models.TextField()
	image = models.ImageField(blank=True, default='default.jpg')
	quoteImage = models.ImageField('Image for Quote Emails', blank=True, default='/static/images/vblogo.jpg')
	organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, null=True, blank=True)
	approved = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse('venue_detail', kwargs={'pk': self.pk})

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

	def __str__(self):			  
		return self.name
	class Meta:
		verbose_name = 'Venue'
		verbose_name_plural = 'My Venues'


class Event_type(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField('description', blank=True)
	active = models.BooleanField()
	seasonal = models.BooleanField()

	def __str__(self):			  
		return self.name
	class Meta:
		verbose_name = 'Event Type'
		verbose_name_plural = 'My Event Types'

class Event_campaign(models.Model):
	name = models.CharField(max_length=50)
	type = models.ForeignKey(Event_type, on_delete=models.CASCADE)
	details = models.TextField('details', blank=True)
	startTime = models.TimeField(blank=True)
	endTime = models.TimeField(blank=True)
	recurring = models.BooleanField()
	image = models.ImageField(blank=True)
	capacity = models.IntegerField()
	cost_per_capacity_unit = models.DecimalField('Cost per person', max_digits=10, decimal_places=2, blank=True, null=True)
	venue = models.ForeignKey(Venue, on_delete=models.CASCADE, blank=True)

	def get_absolute_url(self):
		return reverse('event_campaign_detail', kwargs={'pk': self.pk})

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

	def __str__(self):			  
		return self.name
	class Meta:
		verbose_name = 'Event Campaign'
		verbose_name_plural = 'My Event Campaigns'


class VenueUser(models.Model):
	user = models.OneToOneField(CustomUser, verbose_name="User account details", null=True)
	position = models.CharField(max_length=50, blank=True)
	venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

	def __str__(self):
		return "Venue User " + str(self.user.username)
	class Meta:
		verbose_name = 'Venue User'
		verbose_name_plural = 'My Venue Users'

@receiver(post_save, sender=VenueUser)
def make_VenueUser_staff(sender, **kwargs):
	venueuser = kwargs.get('instance')
	user = venueuser.user
	user.is_staff=True
	user.save()


	
class OrganisationUser(models.Model):
	user = models.OneToOneField(CustomUser, verbose_name="User account details", null=True)
	position = models.CharField(max_length=50, blank=True)
	organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

	def __str__(self):
		return "Organisation User " + str(self.user.username)
	class Meta:
		verbose_name = 'Organisation User'
		verbose_name_plural = 'My Organisation Users' 

@receiver(post_save, sender=OrganisationUser)
def make_OrgUser_staff(sender, **kwargs):
	orguser = kwargs.get('instance')
	user = orguser.user
	user.is_staff=True
	user.save()

class VenuebookerUser(models.Model):
	user = models.OneToOneField(CustomUser, verbose_name="User account details", null=True)

	def __str__(self):
		return str(self.user.username)

class Enquiry(models.Model):
	message = models.TextField()
	attendeeNum = models.IntegerField('Number of Attendees')
	date = models.DateField(blank=False, default=datetime.now)
	event_campaign = models.ForeignKey(Event_campaign, on_delete=models.CASCADE)
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	approved = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse('index')
	def __str__(self):			  
		return str(self.user) + " " + str(self.date)
	class Meta:
		verbose_name = 'Enquiry'
		verbose_name_plural = 'My Enquiries'

class Quote(models.Model):
	description = models.TextField()
	cost = models.FloatField()
	accepted = models.BooleanField(default=False)
	enquiry = models.ForeignKey(Enquiry, on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse('index')
	def __str__(self):			  
		return "Quote for " + str(self.enquiry)
	class Meta:
		verbose_name = 'Quote'
		verbose_name_plural = 'My Quotes'

@receiver(post_save, sender=Quote)
def send_quote_email(sender, **kwargs):
	quote = kwargs.get('instance')
	template_html = 'emails/quote.html'
	template_text = 'emails/quote.txt'
	try:
		subject = 'Quote Received'
		from_email = 'Venuebooker <noreply@venuebooker.com>'
		to = quote.enquiry.user.email
		username = quote.enquiry.user.username
		venue = quote.enquiry.event_campaign.venue
		venue_image = quote.enquiry.event_campaign.venue.quoteImage
		text = get_template(template_text)
		html = get_template(template_html)
		d = {'username': username, 'venue': venue, 'image': venue_image}
		text_content = text.render(d)
		html_content = html.render(d)

		email = EmailMultiAlternatives(subject, text_content, from_email, [to])
		email.attach_alternative(html_content, "text/html")  
		email.content_subtype = 'html'	
		email.mixed_subtype = 'related'					   
		email.send()
	except Exception as e:
		pass

class ContactResponse(models.Model):
	name = models.CharField('name', max_length=300)
	email = models.EmailField('email', max_length=50)
	phone = models.CharField('phone number', max_length=15, blank=True)
	message = models.TextField('message')
	timestamp = models.DateTimeField('timestamp', auto_now_add=True)

	def __str__(self):
		return str(self.id) + " " + self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
	class Meta:
		verbose_name = 'Contact Form Response'
		verbose_name_plural = 'My Contact Form Responses'

class VenueImage(models.Model):
	image = models.ImageField(blank=True)
	venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Venue Image'
		verbose_name_plural = 'My Venue\'s Images'


class EventImage(models.Model):
	image = models.ImageField(blank=True)
	event_campaign = models.ForeignKey(Event_campaign, on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Event Campaign Image'
		verbose_name_plural = 'My Event Campaign\'s Images'

class Lead(models.Model):
	name = models.CharField(max_length=50, blank=False)
	email = models.EmailField('email', max_length=50, blank=False)
	budget = models.DecimalField('Budget', max_digits=10, decimal_places=2, blank=False)
	comments = models.TextField()
	created = models.DateTimeField(_('created'), auto_now_add=True)
	date_from = models.DateField(blank=False)
	date_to = models.DateField(blank=False)
	location = models.CharField(max_length=50, blank=False)
	guests = models.IntegerField(blank=False)
	occasion = models.CharField(max_length=50, blank=False)
	received = models.BooleanField()


	def __str__(self):			  
		return self.name + ' ' + str(self.occasion) + ' ' + str(self.created)
	class Meta:
		verbose_name = 'Lead'
		verbose_name_plural = 'My Leads'
