from datetime import timedelta
from unittest.mock import MagicMock

from django.core.files import File
from django.test import SimpleTestCase, TestCase
from django.utils import timezone

from web_app.forms import ContactForm


class ContactFormTest(SimpleTestCase):

    def test_should_fail_if_form_deemed_invalid_with_valid_data(self):
        form = ContactForm({
            'first_name': 'Joe',
			'last_name': 'Tester',
            'email': 'joe@test.com',
            'telephone': '07865476338',
            'mobile': '01382 786547'
        })
        self.assertTrue(form.is_valid(), 'Form was deemed invalid with valid data')

    def test_should_fail_if_form_deemed_valid_with_blank_data(self):
        form = ContactForm({})
        self.assertFalse(form.is_valid(), 'Form was deemed valid with invalid data')
        self.assertEqual(len(form.errors), 3, 'Different number of errors than expected raised')
        self.assertEqual(form.errors['first_name'], ['This field is required.'], 'Error not raised for empty first_name field')
		self.assertEqual(form.errors['last_name'], ['This field is required.'], 'Error not raised for empty last_name field')
        self.assertEqual(form.errors['email'], ['This field is required.'], 'Error not raised for empty email field')

    def test_should_fail_if_form_deemed_valid_with_invalid_email(self):
        form = ContactForm({
            'name': 'Joe Tester',
            'email': 'joetest.com',
            'phone': '07865476338',
            'message': 'This is a test message'
        })
        self.assertFalse(form.is_valid(), 'Form was deemed valid with invalid data')
        self.assertEqual(len(form.errors), 1, 'Different number of errors than expected raised')
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'],
                         'Error not raised for invalid email field')

class ContactResponseFormTest(SimpleTestCase):

    def test_should_fail_if_form_deemed_invalid_with_valid_data(self):
        form = ContactResponseForm({
            'name': 'Joe Tester',
            'email': 'joe@test.com',
            'phone': '07865476338',
            'message': 'This is a test message'
        })
        self.assertTrue(form.is_valid(), 'Form was deemed invalid with valid data')

    def test_should_fail_if_form_deemed_valid_with_blank_data(self):
        form = ContactResponseForm({})
        self.assertFalse(form.is_valid(), 'Form was deemed valid with invalid data')
        self.assertEqual(len(form.errors), 3, 'Different number of errors than expected raised')
        self.assertEqual(form.errors['name'], ['This field is required.'], 'Error not raised for empty name field')
        self.assertEqual(form.errors['email'], ['This field is required.'], 'Error not raised for empty email field')
        self.assertEqual(form.errors['message'], ['This field is required.'],
                         'Error not raised for empty message field')

    def test_should_fail_if_form_deemed_valid_with_invalid_email(self):
        form = ContactResponseForm({
            'name': 'Joe Tester',
            'email': 'joetest.com',
            'phone': '07865476338',
            'message': 'This is a test message'
        })
        self.assertFalse(form.is_valid(), 'Form was deemed valid with invalid data')
        self.assertEqual(len(form.errors), 1, 'Different number of errors than expected raised')
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'],
                         'Error not raised for invalid email field')
