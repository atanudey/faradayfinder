"""Tests UserSignup form."""

from custom_user.forms.account_forms import UserSignup
from utils.data import SIGNUP_DATA
from django.test import TestCase
from utils.exception import AppMessage


class TestUserSignup(TestCase):
    """Tests UserSignup form."""

    def setUp(self):
        """Creates Setup for class TestUserSignup."""
        self.payload = SIGNUP_DATA.copy()

    def test_signup_without_email(self):
        """Tests signup form without email."""
        del self.payload['email']
        result = UserSignup(self.payload)
        assert result.is_valid() is False
        assert 'email' and 'This field is required.' in result.errors.as_text()

    def test_signup_with_email_value_as_blank(self):
        """Tests signup form if email is blank."""
        self.payload['email'] = ''
        result = UserSignup(self.payload)
        assert result.is_valid() is False
        assert 'email' and 'This field is required' in result.errors.as_text()

    def test_signup_with_invalid_email(self):
        """Tests signup form if email address is invalid."""
        self.payload['email'] = 'test'
        result = UserSignup(self.payload)
        assert result.is_valid() is False
        assert 'email' and 'Enter a valid email address.' in \
                           result.errors.as_text()

    def test_signup_duplicate_email(self):
        """Tests duplicate email."""
        # added a new user
        result = UserSignup(self.payload)
        result.save()

        result1 = UserSignup(self.payload)
        assert result1.is_valid() is False
        assert 'email' and 'A user with that email already exists.' in \
                           result1.errors.as_text()

    def test_first_name_blank(self):
        """Tests signup form with first name as blank value."""
        self.payload['first_name'] = ''
        result = UserSignup(self.payload)
        assert result.is_valid() is False
        assert 'first_name' and 'This field is required.' in \
                                result.errors.as_text()

    def test_first_name_with_max_length_exceeds(self):
        """Tests Signup form if first name is greater than max length."""
        self.payload['first_name'] = "text" * 10
        result = UserSignup(self.payload)
        assert result.is_valid() is False
        assert 'first_name' and 'Ensure this value has at most 20 characters' \
                                in result.errors.as_text()

    def test_last_name_blank(self):
        """Tests signup form with last name as blank value."""
        self.payload['last_name'] = ''
        result = UserSignup(self.payload)
        assert result.is_valid() is False
        assert 'last_name' and 'This field is required.' in \
                               result.errors.as_text()

    def test_first_name_with_max_length_exceeds(self):
        """Tests Signup form if last name is greater than max length."""
        self.payload['last_name'] = "text" * 10
        result = UserSignup(self.payload)
        assert result.is_valid() is False
        assert 'last_name' and 'Ensure this value has at most 20 characters' \
                               in result.errors.as_text()

    def test_zipcode_blank(self):
        """Tests Signup form with zipcode as blank value."""
        self.payload['zipcode'] = ''
        result = UserSignup(self.payload)
        assert result.is_valid() is False
        assert 'zipcode' and 'This field is required.' in \
                             result.errors.as_text()

    def test_zipcode_with_max_length_exceeds(self):
        """Tests Signup form with zipcode as blank value."""
        self.payload['zipcode'] = '12354343453'
        result = UserSignup(self.payload)
        assert result.is_valid() is False
        assert 'zipcode' and \
               AppMessage.error['ZIPCODE_LENGTH_INCORRECT'] in \
               result.errors.as_text()

    def test_zipcode_with_character_value(self):
        """Tests Signup form with zipcode with character value."""
        self.payload['zipcode'] = 'test'
        result = UserSignup(self.payload)
        assert result.is_valid() is False
        print(result.errors.as_text())
        assert 'zipcode' and 'Enter a whole number.' \
                             in result.errors.as_text()

    def test_tnc_with_incorrect_value(self):
        """Tests signup field tnc with incorrect value."""
        self.payload['tnc'] = False
        result = UserSignup(self.payload)
        assert result.is_valid() is False
        assert 'tnc' and \
               AppMessage.error['SIGNUP_AGREE_TNC'] in result.errors.as_text()

    def test_signup_with_password_less_than_6_characters(self):
        """Tests signup form password with value less than 6 characters."""
        self.payload['password'] = 'test'
        result = UserSignup(self.payload)
        assert result.is_valid() is False
        assert 'password' and \
               AppMessage.error['PASSWORD_LENGTH_MIN'] in \
               result.errors.as_text()

    def test_signup_with_password_greater_than_30_characters(self):
        """Tests signup form password with value greater than 30 characters."""
        self.payload['password'] = 'test' * 10
        result = UserSignup(self.payload)
        assert result.is_valid() is False
        assert 'password' and \
               AppMessage.error['PASSWORD_LENGTH_MAX'] in \
               result.errors.as_text()

    def test_with_password_and_confirm_password_not_equal(self):
        """Tests for both passwords match."""
        self.payload['confirm_password'] = 'test'
        self.payload['password'] = 'testing'
        result = UserSignup(self.payload)
        assert result.is_valid() is False
        assert 'confirm_password' and \
               AppMessage.error['PASSWORD_MISMATCH'] in result.errors.as_text()

    def test_signup_form_with_valid_data(self):
        """Tests signup form with valid data."""
        result = UserSignup(self.payload)
        assert result.is_valid() is True
