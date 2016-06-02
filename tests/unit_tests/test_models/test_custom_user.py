""" Tests for signup page. """

import json
import logging
from django.test import TestCase
from custom_user.models import CustomUser
from utils.data import SIGNUP_DATA


LOGGER = logging.getLogger(__name__)


class TestCustomUserModel(TestCase):
    """ Unit test cases for signup page. """

    # def setUp(self):
    #     """Test cases setUp for class TestSignup. """
    #     del SIGNUP_DATA['confirm_password']
    #     self.user = CustomUser.objects.create_user(**SIGNUP_DATA)
    #
    # def tearDown(self):
    #     self.user.delete()
    #
    # def test_create_user(self):
    #     LOGGER.debug(self.user.id)
    #     assert self.user.id == 23
    pass

