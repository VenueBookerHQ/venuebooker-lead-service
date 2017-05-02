import datetime


from django.core.files import File
from django.utils.html import format_html
from django.core.files.storage import Storage
from django.test import TestCase
from django.utils import timezone
from web_app.models import *

class ContactModelTest(TestCase):
	def setUp(self):
		Contact.objects.create(first_name="Joe", last_name="Bloggs", telephone="02890768976", mobile="07716453657",
							   email="j.bloggs@hotmail.com")

	def test_should_fail_if_response_is_not_valid_match(self):
		contact = Contact.objects.get(last_name="Bloggs")
		self.assertEqual(str(contact), "Joe Bloggs", "Contact string representation does not match expected")




def create_organisation():
	Contact.objects.create(first_name="Joe", last_name="Bloggs", telephone="02590768976", mobile="07717453257",
						   email="j.bloggs@hotmail.com")


	organisation = Organisation(name='Hilton Hotels', primary_contact=Contact.objects.all()[0],
								image=None,
								address='1335 6th Ave, New York, NY 10019, USA',
								description='Enjoy breakfast for 2 and in-room WiFi during your stay in NYC '
											'A spectacular location in the heart of Midtown Manhattan '
											'It is all about location in NYC and New York Hilton Midtown places you right in the heart of the action')
	organisation.save()

class OrganisationModelTest(TestCase):
	def setUp(self):
		create_organisation()

	def test_should_fail_if_response_is_not_valid_match(self):
		organisation = Organisation.objects.all()[0]
		self.assertEqual(str(organisation), "Hilton Hotels",
						 "Organisation string representation does not match expected")



class ContactResponseModelTest(TestCase):
	def setUp(self):
		ContactResponse.objects.create(name='Joe', email="joe@tester.com", phone="0389556786", message='Test message')

	def test_should_fail_if_response_is_not_valid_match(self):
		contact_response = ContactResponse.objects.all()[0]
		self.assertEqual(str(contact_response), str(contact_response.id) + " " +
						 contact_response.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
						 "Contact response string representation does not match expected")

def create_venue():
	Contact.objects.create(first_name="Joe", last_name="Bloggs", telephone="02590768976", mobile="07717453257",
						   email="j.bloggs@hotmail.com")

	Organisation.objects.create(name='MacDonald Hotels', primary_contact=Contact.objects.all()[0],
								image=None,
								address='1122 4th Ave, Los Angeles, CA 12019, USA',
								description='Enjoy breakfast for 2 and in-room WiFi during your stay in California '
											'A spectacular location in the heart of Los Angeles '
											'It is all about location in California and the New York Hilton Midtown places you right in the heart of the action')
	venue = Venue(name='MacDonald Los Angeles', address='1122 4th Ave, Los Angeles, CA 12019, USA', facebook_link="", twitter_link="", instagram_link="", description="", image=None, organisation=Organisation.objects.all()[0])
	venue.save()
	

class VenueModelTest(TestCase):
	def setUp(self):
		create_venue()

	def test_should_fail_if_response_is_not_valid_match(self):
		venue = Venue.objects.all()[0]
		self.assertEqual(str(venue), "MacDonald Los Angeles",
						 "Contact response string representation does not match expected")

def create_event_campaign():
	Contact.objects.create(first_name="Joe", last_name="Bloggs", telephone="02590768976", mobile="07717453257",
						   email="j.bloggs@hotmail.com")
	Event_type.objects.create(name="Christmas Dinner", description="This is a Christmas Dinner", active=True, seasonal=True)

	Organisation.objects.create(name='MacDonald Hotels', primary_contact=Contact.objects.all()[0],
								image=None,
								address='1122 4th Ave, Los Angeles, CA 12019, USA',
								description='Enjoy breakfast for 2 and in-room WiFi during your stay in California '
											'A spectacular location in the heart of Los Angeles '
											'It is all about location in California and the New York Hilton Midtown places you right in the heart of the action')
	Venue.objects.create(name='MacDonald Los Angeles', address='1122 4th Ave, Los Angeles, CA 12019, USA', facebook_link="", twitter_link="", instagram_link="", description="", image=None, organisation=Organisation.objects.all()[0])
	event_campaign = Event_campaign(name='MacDonald Los Angeles Christmas Dinner', type=Event_type.objects.all()[0], details="", startTime="12:00:00", endTime="12:00:00", recurring=True, image=None, capacity=40, cost_per_capacity_unit=10, venue=Venue.objects.all()[0])
	event_campaign.save()
	

class Event_campaignModelTest(TestCase):
	def setUp(self):
		create_event_campaign()

	def test_should_fail_if_response_is_not_valid_match(self):
		event_campaign = Event_campaign.objects.all()[0]
		self.assertEqual(str(event_campaign), "MacDonald Los Angeles Christmas Dinner",
						 "Contact response string representation does not match expected")

def create_enquiry():
	Contact.objects.create(first_name="Joe", last_name="Bloggs", telephone="02590768976", mobile="07717453257",
						   email="j.bloggs@hotmail.com")
	CustomUser.objects.create(username="JoeB123", email="j.bloggs@hotmail.com", password="Bloggsy1234", contact=Contact.objects.all()[0])
	Event_type.objects.create(name="Christmas Dinner", description="This is a Christmas Dinner", active=True, seasonal=True)

	Organisation.objects.create(name='MacDonald Hotels', primary_contact=Contact.objects.all()[0],
								image=None,
								address='1122 4th Ave, Los Angeles, CA 12019, USA',
								description='Enjoy breakfast for 2 and in-room WiFi during your stay in California '
											'A spectacular location in the heart of Los Angeles '
											'It is all about location in California and the New York Hilton Midtown places you right in the heart of the action')
	Venue.objects.create(name='MacDonald Los Angeles', address='1122 4th Ave, Los Angeles, CA 12019, USA', facebook_link="", twitter_link="", instagram_link="", description="", image=None, organisation=Organisation.objects.all()[0])
	Event_campaign.objects.create(name='MacDonald Los Angeles Christmas Dinner', type=Event_type.objects.all()[0], details="", startTime="12:00:00", endTime="12:00:00", recurring=True, image=None, capacity=40, cost_per_capacity_unit=10, venue=Venue.objects.all()[0])
	enquiry = Enquiry(message="This is a test Enquiry", attendeeNum=100, date="2017-05-01", event_campaign=Event_campaign.objects.all()[0],
						   user=CustomUser.objects.all()[0], approved=True)
	enquiry.save()
	

class EnquiryModelTest(TestCase):
	def setUp(self):
		create_enquiry()

	def test_should_fail_if_response_is_not_valid_match(self):
		enquiry = Enquiry.objects.all()[0]
		self.assertEqual(str(enquiry), str(enquiry.user) + " " + str(enquiry.date),
						 "Contact response string representation does not match expected")

def create_quote():
	Contact.objects.create(first_name="Joe", last_name="Bloggs", telephone="02590768976", mobile="07717453257",
						   email="j.bloggs@hotmail.com")
	CustomUser.objects.create(username="JoeB123", email="j.bloggs@hotmail.com", password="Bloggsy1234", contact=Contact.objects.all()[0])
	Event_type.objects.create(name="Christmas Dinner", description="This is a Christmas Dinner", active=True, seasonal=True)

	Organisation.objects.create(name='MacDonald Hotels', primary_contact=Contact.objects.all()[0],
								image=None,
								address='1122 4th Ave, Los Angeles, CA 12019, USA',
								description='Enjoy breakfast for 2 and in-room WiFi during your stay in California '
											'A spectacular location in the heart of Los Angeles '
											'It is all about location in California and the New York Hilton Midtown places you right in the heart of the action')
	Venue.objects.create(name='MacDonald Los Angeles', address='1122 4th Ave, Los Angeles, CA 12019, USA', facebook_link="", twitter_link="", instagram_link="", description="", image=None, organisation=Organisation.objects.all()[0])
	Event_campaign.objects.create(name='MacDonald Los Angeles Christmas Dinner', type=Event_type.objects.all()[0], details="", startTime="12:00:00", endTime="12:00:00", recurring=True, image=None, capacity=40, cost_per_capacity_unit=10, venue=Venue.objects.all()[0])
	Enquiry.objects.create(message="Joe", attendeeNum=50, date="2017-08-14", event_campaign=Event_campaign.objects.all()[0],
						   user=CustomUser.objects.all()[0], approved=True)
	quote = Quote(description="This is a test Quote", cost=50, accepted=False, enquiry=Enquiry.objects.all()[0])
	quote.save()
	

class QuoteModelTest(TestCase):
	def setUp(self):
		create_quote()

	def test_should_fail_if_response_is_not_valid_match(self):
		quote = Quote.objects.all()[0]
		self.assertEqual(str(quote), "Quote for " + str(quote.enquiry),
						 "Contact response string representation does not match expected")

def create_event_type():
    event_type = Event_type(name="Christmas Dinner", description="This is a Christmas Dinner", active=True, seasonal=True)
    event_type.save()

class EventTypeModelTest(TestCase):
	def setUp(self):
		create_event_type()

	def test_should_fail_if_response_is_not_valid_match(self):
		event_type = Event_type.objects.all()[0]
		self.assertEqual(str(event_type), "Christmas Dinner",
						 "Event type string representation does not match expected")
def create_venue_user():
    Contact.objects.create(first_name="Joe", last_name="Bloggs", telephone="02590768976", mobile="07717453257",
						   email="j.bloggs@hotmail.com")
    CustomUser.objects.create(username="JoeB123", email="j.bloggs@hotmail.com", password="Bloggsy1234", contact=Contact.objects.all()[0])
    Organisation.objects.create(name='MacDonald Hotels', primary_contact=Contact.objects.all()[0],
								image=None,
								address='1122 4th Ave, Los Angeles, CA 12019, USA',
								description='Enjoy breakfast for 2 and in-room WiFi during your stay in California '
											'A spectacular location in the heart of Los Angeles '
											'It is all about location in California and the New York Hilton Midtown places you right in the heart of the action')
    Venue.objects.create(name='MacDonald Los Angeles', address='1122 4th Ave, Los Angeles, CA 12019, USA', facebook_link="", twitter_link="", instagram_link="", description="", image=None, organisation=Organisation.objects.all()[0])
    venueuser = VenueUser(user=CustomUser.objects.all()[0], position="Manager", venue=Venue.objects.all()[0])
    venueuser.save()

class VenueUserModelTest(TestCase):
	def setUp(self):
		create_venue_user()

	def test_should_fail_if_response_is_not_valid_match(self):
		venue_user = VenueUser.objects.all()[0]
		self.assertEqual(str(venue_user), "Venue User JoeB123",
						 "VenueUser string representation does not match expected")

def create_org_user():
    Contact.objects.create(first_name="Joe", last_name="Bloggs", telephone="02590768976", mobile="07717453257",
						   email="j.bloggs@hotmail.com")
    CustomUser.objects.create(username="JoeB123", email="j.bloggs@hotmail.com", password="Bloggsy1234", contact=Contact.objects.all()[0])
    Organisation.objects.create(name='MacDonald Hotels', primary_contact=Contact.objects.all()[0],
								image=None,
								address='1122 4th Ave, Los Angeles, CA 12019, USA',
								description='Enjoy breakfast for 2 and in-room WiFi during your stay in California '
											'A spectacular location in the heart of Los Angeles '
											'It is all about location in California and the New York Hilton Midtown places you right in the heart of the action')
    orguser= OrganisationUser(user=CustomUser.objects.all()[0], position="Manager", organisation=Organisation.objects.all()[0])
    orguser.save()

class OrganisationUserModelTest(TestCase):
	def setUp(self):
		create_org_user()

	def test_should_fail_if_response_is_not_valid_match(self):
		org_user = OrganisationUser.objects.all()[0]
		self.assertEqual(str(org_user), "Organisation User JoeB123",
						 "OrganisationUser string representation does not match expected")

def create_venuebooker_user():
    Contact.objects.create(first_name="Joe", last_name="Bloggs", telephone="02590768976", mobile="07717453257",
						   email="j.bloggs@hotmail.com")
    CustomUser.objects.create(username="JoeB123", email="j.bloggs@hotmail.com", password="Bloggsy1234", contact=Contact.objects.all()[0])
    vbuser = VenuebookerUser(user=CustomUser.objects.all()[0])
    vbuser.save()

class VenuebookerUserModelTest(TestCase):
	def setUp(self):
		create_venuebooker_user()

	def test_should_fail_if_response_is_not_valid_match(self):
		vb_user = VenuebookerUser.objects.all()[0]
		self.assertEqual(str(vb_user), "JoeB123",
						 "VenuebookerUser string representation does not match expected")

def create_venue_image():
    Contact.objects.create(first_name="Joe", last_name="Bloggs", telephone="02590768976", mobile="07717453257",
						   email="j.bloggs@hotmail.com")
    CustomUser.objects.create(username="JoeB123", email="j.bloggs@hotmail.com", password="Bloggsy1234", contact=Contact.objects.all()[0])
    Organisation.objects.create(name='MacDonald Hotels', primary_contact=Contact.objects.all()[0],
								image=None,
								address='1122 4th Ave, Los Angeles, CA 12019, USA',
								description='Enjoy breakfast for 2 and in-room WiFi during your stay in California '
											'A spectacular location in the heart of Los Angeles '
											'It is all about location in California and the New York Hilton Midtown places you right in the heart of the action')
    Venue.objects.create(name='MacDonald Los Angeles', address='1122 4th Ave, Los Angeles, CA 12019, USA', facebook_link="", twitter_link="", instagram_link="", description="", image=None, organisation=Organisation.objects.all()[0])
    venue_image = VenueImage(image="default.jpg", venue=Venue.objects.all()[0])
    venue_image.save()

class VenueImageModelTest(TestCase):
	def setUp(self):
		create_venue_image()

	def test_should_fail_if_response_is_not_valid_match(self):
		venue_image = VenueImage.objects.all()[0]
		self.assertEqual(str(venue_image), "VenueImage object",
						 "VenueImage string representation does not match expected")

def create_event_image():
    Contact.objects.create(first_name="Joe", last_name="Bloggs", telephone="02590768976", mobile="07717453257",
						   email="j.bloggs@hotmail.com")
    CustomUser.objects.create(username="JoeB123", email="j.bloggs@hotmail.com", password="Bloggsy1234", contact=Contact.objects.all()[0])
    Organisation.objects.create(name='MacDonald Hotels', primary_contact=Contact.objects.all()[0],
								image=None,
								address='1122 4th Ave, Los Angeles, CA 12019, USA',
								description='Enjoy breakfast for 2 and in-room WiFi during your stay in California '
											'A spectacular location in the heart of Los Angeles '
											'It is all about location in California and the New York Hilton Midtown places you right in the heart of the action')
    Venue.objects.create(name='MacDonald Los Angeles', address='1122 4th Ave, Los Angeles, CA 12019, USA', facebook_link="", twitter_link="", instagram_link="", description="", image=None, organisation=Organisation.objects.all()[0])
    Event_type.objects.create(name="Christmas Dinner", description="This is a Christmas Dinner", active=True, seasonal=True)
    Event_campaign.objects.create(name='MacDonald Los Angeles Christmas Dinner', type=Event_type.objects.all()[0], details="", startTime="12:00:00", endTime="12:00:00", recurring=True, image=None, capacity=40, cost_per_capacity_unit=10, venue=Venue.objects.all()[0])
    event_image = EventImage(image="default.jpg", event_campaign=Event_campaign.objects.all()[0])
    event_image.save()

class EventImageModelTest(TestCase):
	def setUp(self):
		create_event_image()

	def test_should_fail_if_response_is_not_valid_match(self):
		event_image = EventImage.objects.all()[0]
		self.assertEqual(str(event_image), "EventImage object",
						 "EventImage string representation does not match expected")

def create_lead():
    lead = Lead(name="Joe Bloggs", email="j.bloggs@hotmail.com", budget=500.00, comments="This is a comment", date_from="2017-08-12", date_to="2017-09-12", location="Dundee", guests=50, occasion="Private Party", received=True)
    lead.save()

class LeadModelTest(TestCase):
	def setUp(self):
		create_lead()

	def test_should_fail_if_response_is_not_valid_match(self):
		lead = Lead.objects.all()[0]
		self.assertEqual(str(lead), 'Joe Bloggs' + ' ' + 'Private Party' + ' ' + str(lead.created),
						 "Lead string representation does not match expected")



