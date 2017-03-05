import datetime

from unittest.mock import MagicMock

from django.core.files import File
from django.core.files.storage import Storage
from django.test import TestCase
from django.utils import timezone
from web_app.models import Contact, ContactResponse, Organisation

class ContactModelTest(TestCase):
    def setUp(self):
        Contact.objects.create(first_name="Joe", surname="Bloggs", telephone="02890768976", mobile="07716453657",
                               email="j.bloggs@hotmail.com")

    def test_should_fail_if_response_is_not_valid_match(self):
        contact = Contact.objects.get(surname="Bloggs")
        self.assertEqual(str(contact), "Bloggs", "Contact string representation does not match expected")




def create_organisation():
    Contact.objects.create(first_name="Joe", surname="Bloggs", telephone="02590768976", mobile="07717453257",
                           email="j.bloggs@hotmail.com")

    file_mock = mock.MagicMock(spec=File, name='FileMock')
    file_mock.name = 'test.jpg'

    organisation = Organisation(name='Hilton Hotels', primary_contact=Contact.objects.all()[0],
                                image=file_mock,
                                address='1335 6th Ave, New York, NY 10019, USA',
                                description='Enjoy breakfast for 2 and in-room WiFi during your stay in NYC '
                                            'A spectacular location in the heart of Midtown Manhattan '
                                            'It is all about location in NYC and New York Hilton Midtown places you right in the heart of the action')
    storage_mock = mock.MagicMock(spec=Storage, name='StorageMock')
    storage_mock.save = mock.MagicMock(name='save')
    storage_mock.save.return_value = '/tmp/test1.jpg'

    with mock.patch('django.core.files.storage.default_storage._wrapped', storage_mock):
        organisation.save()

class OrganisationModelTest(TestCase):
    def setUp(self):
        create_organisation()

    def test_should_fail_if_response_is_not_valid_match(self):
        organisation = Organisation.objects.all()[0]
        self.assertEqual(str(organisation), str(organisation.id) + " " + "Hilton Hotels",
                         "Organisation string representation does not match expected")

    def test_image_preview_large_valid_logo(self):
        organisation = Organisation.objects.all()[0]
        self.assertEqual(organisation.image_preview_large(), '<img src="/tmp/test1.jpg" width="150" height="150"/>',
                         "Generated html does not match expected")

    def test_image_preview_large_no_logo(self):
        organisation = Organisation.objects.all()[0]
        organisation.image = None
        self.assertEqual(organisation.image_preview_large(), 'No Logo',
                         "Response does not match expected")

    def test_image_preview_small_valid_logo(self):
        organisation = Organisation.objects.all()[0]
        self.assertEqual(organisation.image_preview_small(), '<img src="/tmp/test1.jpg" width="50" height="50"/>',
                         "Generated html does not match expected")

    def test_image_preview_small_no_logo(self):
        organisation = Organisation.objects.all()[0]
        organisation.image = None
        self.assertEqual(organisation.image_preview_small(), 'No Logo',
                         "Response does not match expected")


class ContactResponseTest(TestCase):
    def setUp(self):
        ContactResponse.objects.create(name='Joe', email="joe@tester.com", phone="0389556786", message='Test message')

    def test_should_fail_if_response_is_not_valid_match(self):
        contact_response = ContactResponse.objects.all()[0]
        self.assertEqual(str(contact_response), str(contact_response.id) + " " +
                         contact_response.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                         "Contact response string representation does not match expected")

