""" Tests for signup page. """

import json
import logging
from mock import patch, Mock
from django.test import TestCase, Client
from utils.exception import AppMessage
from utils.data import SIGNUP_DATA
from custom_user.views.views_accounts import UserSignup
from custom_user.models import CustomUser
from unittest.mock import MagicMock
from django.http import HttpRequest


LOGGER = logging.getLogger(__name__)


class TestSignup(TestCase):
    """ Unit test cases for signup page. """

    def setUp(self):
        """Test cases setUp for class TestSignup. """

        self.client = Client()
        self.url = '/accounts/signup/'
        self.payload = SIGNUP_DATA

        self.request = HttpRequest()

    def tearDown(self):
        CustomUser.objects.all().delete()

    def test_signup_without_ajax_call(self):
        """Tests if submit form without ajax call. """

        request = self.client.post(self.url, {})
        response = json.loads(request.content.decode())
        assert response['result'] is False
        assert response['message'] == AppMessage.error['INVALID_REQUEST']

    def test_signup_with_invalid_email(self):
        """Tests signup page with email is invalid. """
        self.payload['email'] = ''
        request = self.client.post(self.url, self.payload,
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        response = json.loads(request.content.decode())
        assert response['result'] is False
        assert response['email'][0] == 'This field is required.'

    @patch('utils.common.Email.go_email')
    def test_mock_email_for_user_signup(self, mock_email):
        """Mocks email function when registering a user. """
        self.request.__setattr__('HTTP_X_REQUESTED_WITH', 'XMLHttpRequest')
        self.request.__setattr__('method', 'POST')
        self.request.is_ajax = MagicMock(return_value=True)
        self.request.POST.update(self.payload)

        # view
        view = UserSignup()
        view.request = self.request
        mock_email.return_value = True
        response = view.post(self.request)
        content = json.loads(response.content.decode())

        assert response.status_code == 201
        assert content['result'] is True
        assert content['message'] == AppMessage.success['SIGNUP_SUCCESS']
