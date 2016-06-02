"""
Tests common utils
"""
from django.test import TestCase, Client
from utils import common


class TestUtils(TestCase):
    """Tests common utils."""

    def setUp(self):
        self.client = Client()

    def test_random(self):
        assert len(common.random_number(32)) == 32

    def test_encode_decode(self):
        input_value = 'Testing'
        encoded_value = common.encode(input_value)
        assert common.decode(encoded_value) == input_value

    # def test_email(self):
    #     request = self.client.get('/')
    #     data = {
    #         'email': 'test@test.com',
    #
    #     }
    #     email = common.Email.go_email(request)
    #     assert email == None



