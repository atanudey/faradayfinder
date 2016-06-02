"""
This File contains information about forms profile related
"""

import logging
from django import forms
from custom_user.models import Country
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from utils.exception import AppMessage

LOGGER = logging.getLogger(__name__)


class EditProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'input_bg'
        self.fields['last_name'].widget.attrs['class'] = 'input_bg'
        self.fields['zipcode'].widget.attrs['class'] = 'input_bg'
        # self.fields['about_me'].widget.attrs['class'] = 'input_bg'
        self.fields['about_me'].widget.attrs['rows'] = '7'
        self.fields['about_me'].widget.attrs['cols'] = '77'
        self.fields['address'].widget.attrs['class'] = 'input'
        self.fields['city'].widget.attrs['class'] = 'input_bg'
        self.fields['state'].widget.attrs['class'] = 'input_bg'
        self.fields['country'].widget.attrs['class'] = 'input_bg'
        self.fields['dob'].widget.attrs['class'] = 'input_bg'

    def clean_dob(self):
        dob = self.cleaned_data.get('dob')
        if not dob:
            return None
        return dob

    def clean_country(self):
        country = self.cleaned_data.get('country')
        try:
            return Country.objects.get(name=country)
        except Country.DoesNotExist:
            raise forms.ValidationError(
                'Country does not exist.'
            )

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'about_me', 'zipcode',
                  'address', 'city', 'state', 'country', 'dob']


class EditNetwork(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditNetwork, self).__init__(*args, **kwargs)

        fields_dropdown = ['is_phone_public', 'is_facebook_public',
                           'is_linkedin_public', 'is_skype_public',
                           'is_twitter_public',  'is_aim_public']
        fields_textbox = ['phone', 'facebook', 'linkedin', 'skype',
                          'twitter', 'aim']

        for f in fields_dropdown:
            self.fields[f].widget.attrs['class'] = 'Textinput'
            self.fields[f].widget.attrs['style'] = \
                'margin-right:15px; width:83px; height:24px;'

        for f in fields_textbox:
            self.fields[f].widget.attrs['class'] = 'input'
            self.fields[f].widget.attrs['style'] = 'width: 200px'
            self.fields[f].widget.attrs['maxlength'] = '128'
            self.fields[f].widget.attrs['size'] = '32'

    class Meta:
        model = get_user_model()
        fields = ['is_phone_public', 'phone', 'is_facebook_public', 'facebook',
                  'is_linkedin_public', 'linkedin', 'is_skype_public', 'skype',
                  'is_twitter_public', 'twitter', 'is_aim_public', 'aim',
                  'photo', 'resume']


class EditPassword(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditPassword, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['class'] = 'input_bg'
        self.fields['new_password'].widget.attrs['class'] = 'input_bg'
        self.fields['confirm_new_password'].widget.attrs['class'] = \
            'input_bg'
        self.fields['password'].widget.attrs['placeholder'] = \
            'Enter your current password'
        self.fields['new_password'].widget.attrs['placeholder'] = \
            'Enter your new password'
        self.fields['confirm_new_password'].widget.attrs['placeholder'] = \
            'Confirm your new password'

    password = forms.CharField(
        label=_("Old Password"),
        widget=forms.PasswordInput
    )

    new_password = forms.CharField(
        label=_("New Password"),
        widget=forms.PasswordInput,
        help_text=_("Enter new password.")
    )

    confirm_new_password = forms.CharField(
        label=_("New Password"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification.")
    )

    def clean_new_password(self):
        """Cleans password
        :return: str password
        :raise forms.ValidationError: if password length is not correct.
        """
        new_password = self.cleaned_data.get('new_password')
        if len(new_password) < 6:
            raise forms.ValidationError(
                AppMessage.error['PASSWORD_LENGTH_MIN']
            )
        elif len(new_password) > 30:
            raise forms.ValidationError(
                AppMessage.error['PASSWORD_LENGTH_MAX']
            )
        return new_password

    def clean_confirm_new_password(self):
        """Cleans confirm password
        :return: str confirm password
        :raise forms.ValidationError: if both passwords are not equals
        """
        new_password = self.cleaned_data.get('new_password')
        confirm_new_password = self.cleaned_data.get('confirm_new_password')
        if new_password != confirm_new_password:
            raise forms.ValidationError(
                AppMessage.error['PASSWORD_MISMATCH']
            )

        return new_password

    class Meta:
        model = get_user_model()
        fields = ['password', 'new_password', 'confirm_new_password']
