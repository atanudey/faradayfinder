""" Tests cases for pages. """

from django.test import TestCase, Client


class TestPages(TestCase):
    """ Test cases for static and dynamic pages. """

    def setUp(self):
        """ Defines Setup for TestPages. """

        self.client = Client()

    def test_home_page(self):
        """ Tests home page. """

        result = self.client.get('/')
        assert result.status_code == 200
        assert 'Feature events' in result.content.decode('utf-8')

    def test_about_us_page(self):
        """Tests about us page. """

        result = self.client.get('/about-us/')
        assert result.status_code == 200
        assert 'About us' in result.content.decode('utf-8')

    def test_contact_us_page(self):
        """Tests contact us page. """

        result = self.client.get('/contact-us/')
        assert result.status_code == 200
        assert 'Contact us' in result.content.decode('utf-8')

    def test_signup_page(self):
        """Tests login pages. """

        result = self.client.get('/accounts/signup/')
        assert result.status_code == 200
        assert 'Register now' in result.content.decode('utf-8')

    def test_faq_page(self):
        """Tests FAQ page."""

        result = self.client.get('/faq/')
        assert result.status_code == 200
        assert 'Frequently asked questions' in result.content.decode('utf-8')

    def test_terms_and_conditions_page(self):
        """Tests Terms and Conditions Page."""

        result = self.client.get('/terms-and-conditions/')
        assert result.status_code == 200
        assert 'Terms and Conditions' in result.content.decode('utf-8')

    def test_privacy_and_policy(self):
        result = self.client.get('/privacy-and-policy/')
        assert result.status_code == 200
        assert 'Privacy and Policy' in result.content.decode('utf-8')
