from django.core.urlresolvers import reverse
from django.test import SimpleTestCase, TestCase

from web_app.models import ContactResponse


class IndexViewTest(SimpleTestCase):

    def test_should_fail_if_valid_response_not_returned_for_index_request(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200, 'Status code not 200')
        self.assertTemplateUsed(response, "index.html", 'Index template not returned')


class TermsViewTest(SimpleTestCase):

    def test_should_fail_if_valid_response_not_returned_for_terms_request(self):
        response = self.client.get(reverse('terms'))
        self.assertEqual(response.status_code, 200, 'Status code not 200')
        self.assertTemplateUsed(response, "terms.html", 'Contact template not returned')

class PrivacyViewTest(SimpleTestCase):

    def test_should_fail_if_valid_response_not_returned_for_terms_request(self):
        response = self.client.get(reverse('privacy'))
        self.assertEqual(response.status_code, 200, 'Status code not 200')
        self.assertTemplateUsed(response, "privacy.html", 'Privacy Policy template not returned')

class LoginViewTest(SimpleTestCase):

    def test_should_fail_if_valid_response_not_returned_for_login_request(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200, 'Status code not 200')
        self.assertTemplateUsed(response, "web_app/login_form.html", 'Login template not returned')

class LogoutViewTest(TestCase):
    fixtures = ['initial_data']

    def test_should_fail_if_valid_response_not_returned_for_logout_request(self):
        self.client.login(username='welcomeuser', password='welcomepassword')
        response = self.client.get(reverse('logout_user'))
        self.assertEqual(response.status_code, 200, 'Status code not 200')
        self.assertTemplateUsed(response, "web_app/login_form.html", 'Login template not returned')

class RegisterViewTest(SimpleTestCase):

    def test_should_fail_if_valid_response_not_returned_for_register_request(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200, 'Status code not 200')
        self.assertTemplateUsed(response, "web_app/register_form.html", 'Register template not returned')

class VenueSignupViewTest(TestCase):
    fixtures = ['initial_data']

    def test_should_fail_if_valid_response_not_returned_for_venue_signup_request(self):
        self.client.login(username='welcomeuser', password='welcomepassword')
        response = self.client.get(reverse('venue_signup_info'))
        self.assertEqual(response.status_code, 200, 'Status code not 200')
        self.assertTemplateUsed(response, "venue_signup.html", 'Venue signup template not returned')

class UpdateProfileViewTest(TestCase):
    fixtures = ['initial_data']

    def test_should_fail_if_valid_response_not_returned_for_update_profile_request(self):
        self.client.login(username='welcomeuser', password='welcomepassword')
        response = self.client.get(reverse('profile-update'))
        self.assertEqual(response.status_code, 200, 'Status code not 200')
        self.assertTemplateUsed(response, "web_app/customuser_form.html", 'Profile Update template not returned')

class ChangePasswordViewTest(TestCase):
    fixtures = ['initial_data']

    def test_should_fail_if_valid_response_not_returned_for_update_profile_request(self):
        self.client.login(username='welcomeuser', password='welcomepassword')
        response = self.client.get(reverse('change_password'))
        self.assertEqual(response.status_code, 200, 'Status code not 200')
        self.assertTemplateUsed(response, "web_app/change_password.html", 'Password Change template not returned')

class ContactViewTest(TestCase):

    def setUp(self):
        self.num_responses = ContactResponse.objects.count()

    def test_should_fail_if_valid_response_not_returned_for_contact_request(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200, 'Status code not 200')
        self.assertTemplateUsed(response, "contact.html", 'Contact template not returned')

    def test_should_fail_if_error_not_returned_for_empty_message_in_post(self):
        self.assertEqual(self.num_responses, 0, 'Initial number of contact responses not 0')
        response = self.client.post(reverse('contact'), {'name': 'Joe Bloggs', 'email': 'joe@hotmail.com',
                                                         'phone': '01274639493', 'message': ''})
        self.assertEqual(response.status_code, 200, 'Status code not 200')
        self.assertFormError(response, 'form', 'message', 'This field is required.', 'Error message not present for'
                                                                                     'message field')
        self.assertEqual(ContactResponse.objects.count(), self.num_responses, 'Number of responses has changed')

    def test_should_fail_if_error_not_returned_for_invalid_email_in_post(self):
        self.assertEqual(self.num_responses, 0, 'Initial number of contact responses not 0')
        response = self.client.post(reverse('contact'), {'name': 'Joe Bloggs', 'email': 'joehotmail.com',
                                                         'phone': '01274639493', 'message': 'Test message'})
        self.assertEqual(response.status_code, 200, 'Status code not 200')
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.', 'Error message not present for'
                                                                                        'email field')
        self.assertEqual(ContactResponse.objects.count(), self.num_responses, 'Number of responses has changed')

    def test_should_fail_if_contact_responses_not_increased_for_valid_post(self):
        response = self.client.post(reverse('contact'), {'name': 'Joe Bloggs', 'email': 'joe@hotmail.com',
                                                         'phone': '02893838943', 'message': 'Test message'},
                                    follow=True)
        self.assertEqual(ContactResponse.objects.count(), self.num_responses + 1,
                         'Number of contact responses in db not'
                         'increased by 1')
        self.assertEqual(len(response.redirect_chain), 1, "Not 1 redirect in redirect chain")
        self.assertEqual(response.redirect_chain[0][0], reverse('contact'), 'Initial redirect url not contact page')
        self.assertEqual(response.redirect_chain[0][1], 302, 'Initial status code not 302')
        self.assertEqual(response.status_code, 200, 'Final status code not 200')

class VenuesViewTest(TestCase):
    fixtures = ['initial_data']

    def test_should_fail_if_valid_response_not_returned_for_venues_request(self):
        self.client.login(username='welcomeuser', password='welcomepassword')
        response = self.client.get(reverse('venue_list'))
        self.assertEqual(response.status_code, 200, 'Status code not 200')
        self.assertTemplateUsed(response, "venues.html", 'Venues '
                                                                       'template not returned')
        self.assertEqual(len(response.context['object_list']), 2, 'Two venues in db not sent to template')


class VenueProfileViewTest(TestCase):
    fixtures = ['initial_data']

    def test_should_fail_if_valid_response_not_returned_for_venue_with_id_one(self):
        self.client.login(username='welcomeuser', password='welcomepassword')
        response = self.client.get(reverse('venue_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200, 'Status code not 200')
        self.assertTemplateUsed(response, "venue_detail.html", 'Venue template not'
                                                                      'returned')
        self.assertEqual(response.context['venue'].id, 1, 'Venue with id 1 not sent to template')

    def test_should_fail_if_valid_response_not_returned_for_non_existent_venue_id(self):
        self.client.login(username='welcomeuser', password='welcomepassword')
        response = self.client.get(reverse('venue_detail', kwargs={'pk': 6}))
        self.assertEqual(response.status_code, 404, 'Status code not 404')

    def test_should_fail_if_valid_response_not_returned_for_venue_not_approved(self):
        self.client.login(username='welcomeuser', password='welcomepassword')
        response = self.client.get(reverse('venue_detail', kwargs={'pk': 3}))
        self.assertEqual(response.status_code, 200, 'Status code not 200')
        self.assertTemplateUsed(response, 'index.html', 'Index template not returned')


class EventCampaignListViewTest(TestCase):
    fixtures = ['initial_data']

    def test_should_fail_if_valid_response_not_returned_for_event_campaign_listing_request(self):
        self.client.login(username='welcomeuser', password='welcomepassword')
        response = self.client.get(reverse('event_campaign_list'))
        self.assertEqual(response.status_code, 200, 'Status code not 200')
        self.assertTemplateUsed(response, "eventcampaigns.html", 'Event listing '
                                                                       'template not returned')
        self.assertEqual(len(response.context['object_list']), 2, 'Two event campaigns in db not sent to template')


class EventCampaignViewTest(TestCase):
    fixtures = ['initial_data']

    def test_should_fail_if_valid_response_not_returned_for_event_campaign_with_id_one(self):
        self.client.login(username='welcomeuser', password='welcomepassword')
        response = self.client.get(reverse('event_campaign_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200, 'Status code not 200')
        self.assertTemplateUsed(response, "event_campaign_detail.html", 'Event_campaign template not'
                                                                      'returned')
        self.assertEqual(response.context['event_campaign'].id, 1, 'Event Campaign with id 1 not sent to template')

    def test_should_fail_if_valid_response_not_returned_for_non_existent_event_campaign_id(self):
        self.client.login(username='welcomeuser', password='welcomepassword')
        response = self.client.get(reverse('event_campaign_detail', kwargs={'pk': 6}))
        self.assertEqual(response.status_code, 404, 'Status code not 404')

class ProfileTest(TestCase):
    fixtures = ['initial_data']

    def test_should_fail_if_login_redirect_not_performed_for_incorrect_user_credentials_users(self):
        self.client.login(username='welcomeuser', password='welcomepword')
        response = self.client.get(reverse('profile'), follow=True)
        self.assertEqual(response.status_code, 200, "Final status code not 200")
        self.assertEqual(len(response.redirect_chain), 1, "Not 1 redirect in redirect chain")
        self.assertEqual(response.redirect_chain[0][0], "%s?next=%s" % (reverse('login'),
                                                                        reverse('profile')),
                         "Initial redirect url not login page")
        self.assertEqual(response.redirect_chain[0][1], 302, "Initial status code not 302")
        self.assertTemplateUsed(response, 'web_app/login_form.html', 'Login template not used in response')

    def test_should_fail_if_login_redirect_not_performed_for_unauthenticated_users(self):
        response = self.client.get(reverse('profile'), follow=True)
        self.assertEqual(response.status_code, 200, "Final status code not 200")
        self.assertEqual(len(response.redirect_chain), 1, "Not 1 redirect in redirect chain")
        self.assertEqual(response.redirect_chain[0][0], "%s?next=%s" % (reverse('login'),
                                                                        reverse('profile')),
                         "Initial redirect url not"
                         "login page")
        self.assertEqual(response.redirect_chain[0][1], 302, "Initial status code not 302")
        self.assertTemplateUsed(response, 'web_app/login_form.html', 'Login template not used in response')

class LoginViewTest(TestCase):
    fixtures = ['initial_data']

    def setUp(self):
        self.admin_user = {'username': 'admin_user',
                           'password': 'bcadminpass123'}
        self.standard_user = {'username': 'welcomeuser',
                              'password': 'welcomepassword'}
        self.invalid_user1 = {'username': 'inval_user',
                              'password': 'edfsdgf'}
        self.invalid_user2 = {'username': 'welcomeuser1',
                              'password': 'inval_pass'}

    def test_should_fail_if_valid_response_not_returned_for_login_request(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200, 'Status code not 200')
        self.assertTemplateUsed(response, 'web_app/login_form.html', 'Login template not returned')

    def test_should_fail_if_admin_user_not_redirected_to_admin_page(self):
        response = self.client.post(reverse('login'), self.admin_user, follow=True)
        self.assertEqual(len(response.redirect_chain), 2, 'Redirect chain not a length of 2')
        self.assertEqual(response.redirect_chain[0][1], 302, 'Initial redirect status code not 302')
        self.assertEqual(response.redirect_chain[1][0], reverse('admin:index'), 'Second redirect url not admin page')
        self.assertTemplateUsed(response, 'admin/index.html', 'Admin template not used in response.')
        self.assertEqual(response.status_code, 200, 'Final status code not 200')

    def test_should_fail_if_standard_user_not_redirected_to_profile(self):
        response = self.client.post(reverse('login'), self.standard_user, follow=True)
        self.assertEqual(len(response.redirect_chain), 1, 'Redirect chain not a length of 1')
        self.assertEqual(response.redirect_chain[0][0], reverse('index'), 'Redirect url not index')
        self.assertEqual(response.redirect_chain[0][1], 302, 'Redirect code not 302')
        self.assertTemplateUsed(response, 'index.html', 'Index template not used in response')
        self.assertEqual(response.status_code, 200, 'Final status code not 200')

    def test_should_fail_if_invalid_username_password_cause_redirect(self):
        response = self.client.post(reverse('login'), self.invalid_user1, follow=True)
        self.assertEqual(len(response.redirect_chain), 0, 'Redirect chain not empty')
        self.assertEqual(response.status_code, 200, 'Final status code not 200')

    def test_should_fail_if_valid_username_invalid_password_cause_redirect(self):
        response = self.client.post(reverse('login'), self.invalid_user2, follow=True)
        self.assertEqual(len(response.redirect_chain), 0, 'Redirect chain not empty')
        self.assertEqual(response.status_code, 200, 'Final status code not 200')

