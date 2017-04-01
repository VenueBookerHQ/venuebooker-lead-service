import datetime

from unittest.mock import MagicMock
from unittest.mock import patch

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

    organisation.object.create(name='MacDonald Hotels', primary_contact=Contact.objects.all()[0],
                                image=None,
                                address='1122 4th Ave, Los Angeles, CA 12019, USA',
                                description='Enjoy breakfast for 2 and in-room WiFi during your stay in California '
                                            'A spectacular location in the heart of Los Angeles '
                                            'It is all about location in California and the New York Hilton Midtown places you right in the heart of the action')
    venue = Venue(name='MacDonald Los Angeles', address='1122 4th Ave, Los Angeles, CA 12019, USA', facebook_link="", facebook_link="", facebook_link="", description="", image=None, organisation=Organisation.objects.all()[0])
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

    Organisation.object.create(name='MacDonald Hotels', primary_contact=Contact.objects.all()[0],
                                image=None,
                                address='1122 4th Ave, Los Angeles, CA 12019, USA',
                                description='Enjoy breakfast for 2 and in-room WiFi during your stay in California '
                                            'A spectacular location in the heart of Los Angeles '
                                            'It is all about location in California and the New York Hilton Midtown places you right in the heart of the action')
    Venue.object.create(name='MacDonald Los Angeles', address='1122 4th Ave, Los Angeles, CA 12019, USA', facebook_link="", facebook_link="", facebook_link="", description="", image=None, organisation=Organisation.objects.all()[0])
    event_campaign = Event_campaign(name='MacDonald Los Angeles Christmas Dinner', type=Event_type.objects.all()[0], details="", startTime="", endTime="", recurring=True, image=None, capacity=40, cost_per_capacity_unit=10, venue=Venue.objects.all()[0])
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
    Event_type.objects.create(name="Christmas Dinner", description="This is a Christmas Dinner", active=True, seasonal=True)

    Organisation.object.create(name='MacDonald Hotels', primary_contact=Contact.objects.all()[0],
                                image=None,
                                address='1122 4th Ave, Los Angeles, CA 12019, USA',
                                description='Enjoy breakfast for 2 and in-room WiFi during your stay in California '
                                            'A spectacular location in the heart of Los Angeles '
                                            'It is all about location in California and the New York Hilton Midtown places you right in the heart of the action')
    Venue.object.create(name='MacDonald Los Angeles', address='1122 4th Ave, Los Angeles, CA 12019, USA', facebook_link="", facebook_link="", facebook_link="", description="", image=None, organisation=Organisation.objects.all()[0])
    Event_campaign.object.create(name='MacDonald Los Angeles Christmas Dinner', type=Event_type.objects.all()[0], details="", startTime="", endTime="", recurring=True, image=None, capacity=40, cost_per_capacity_unit=10, venue=Venue.objects.all()[0])
    enquiry = Enquiry(message="Joe", attendeeNum="Bloggs", date="02590768976", event_campaign=Event_campaign.objects.all()[0],
                           user=#########, approved=True)
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
    Event_type.objects.create(name="Christmas Dinner", description="This is a Christmas Dinner", active=True, seasonal=True)

    Organisation.object.create(name='MacDonald Hotels', primary_contact=Contact.objects.all()[0],
                                image=None,
                                address='1122 4th Ave, Los Angeles, CA 12019, USA',
                                description='Enjoy breakfast for 2 and in-room WiFi during your stay in California '
                                            'A spectacular location in the heart of Los Angeles '
                                            'It is all about location in California and the New York Hilton Midtown places you right in the heart of the action')
    Venue.object.create(name='MacDonald Los Angeles', address='1122 4th Ave, Los Angeles, CA 12019, USA', facebook_link="", facebook_link="", facebook_link="", description="", image=None, organisation=Organisation.objects.all()[0])
    Event_campaign.object.create(name='MacDonald Los Angeles Christmas Dinner', type=Event_type.objects.all()[0], details="", startTime="", endTime="", recurring=True, image=None, capacity=40, cost_per_capacity_unit=10, venue=Venue.objects.all()[0])
    Enquiry.object.create(message="Joe", attendeeNum="Bloggs", date="02590768976", event_campaign=Event_campaign.objects.all()[0],
                           user=#########, approved=True)
    quote = Quote(description="Joe", cost="Bloggs", accepted="02590768976", enquiry=Enquiry.objects.all()[0])
    quote.save()
    

class QuoteModelTest(TestCase):
    def setUp(self):
        create_quote()

    def test_should_fail_if_response_is_not_valid_match(self):
        quote = Quote.objects.all()[0]
        self.assertEqual(str(quote), "Quote for" + str(quote.enquiry),
                         "Contact response string representation does not match expected")



