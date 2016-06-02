""" EmailUser forms."""

import logging
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _
from utils.exception import AppMessage

LOGGER = logging.getLogger(__name__)


class EmailUserCreationForm(forms.ModelForm):

    """ A form for creating new users.
    Includes all the required fields, plus a repeated password.
    """

    error_messages = {
        'duplicate_email': _("A user with that email already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }

    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = get_user_model()
        fields = ('email',)

    def clean_email(self):
        """ Clean form email.
        :return str email: cleaned email
        :raise forms.ValidationError: Email is duplicated
        """
        # Since EmailUser.email is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        email = self.cleaned_data["email"]
        try:
            get_user_model()._default_manager.get(email=email)
        except get_user_model().DoesNotExist:
            return email

        raise forms.ValidationError(
            AppMessage.error['DUPLICATE_EMAIL'],
            code='duplicate_email',
        )

    def clean_password2(self):
        """ Check that the two password entries match.
        :return str password2: cleaned password2
        :raise forms.ValidationError: password2 != password1
        """
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        """ Save user.
        Save the provided password in hashed format.
        :return custom_user.models.EmailUser: user
        """
        user = super(EmailUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class EmailUserChangeForm(forms.ModelForm):

    """ A form for updating users.
    Includes all the fields on the user, but replaces the password field
    with admin's password hash display field.
    """

    password = ReadOnlyPasswordHashField(label=_("Password"), help_text=_(
        "Raw passwords are not stored, so there is no way to see "
        "this user's password, but you can change the password "
        "using <a href=\"password/\">this form</a>."))

    class Meta:
        model = get_user_model()
        exclude = ()

    def __init__(self, *args, **kwargs):
        """ Init the form."""
        super(EmailUserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def clean_password(self):
        """ Clean password.
        Regardless of what the user provides, return the initial value.
        This is done here, rather than on the field, because the
        field does not have access to the initial value.
        :return str password:
        """
        return self.initial["password"]


class UserSignup(forms.ModelForm):
    """
    A form for user signup.
    Includes fields first name, last name, email, password, tnc name zipcode
    """
    password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput
    )
    confirm_password = forms.CharField(
        label=_("Confirm Password"),
        widget=forms.PasswordInput
    )

    def __init__(self, *args, **kwargs):
        super(UserSignup, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = \
            'form-control input-normal'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['confirm_password'].widget.attrs['class'] = 'form-control'
        self.fields['zipcode'].widget.attrs['class'] = 'form-control'

    def clean_password(self):
        """Cleans password
        :return: str password
        :raise forms.ValidationError: if password length is not correct.
        """
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise forms.ValidationError(
                AppMessage.error['PASSWORD_LENGTH_MIN']
            )
        elif len(password) > 30:
            raise forms.ValidationError(
                AppMessage.error['PASSWORD_LENGTH_MAX']
            )
        return password

    def clean_confirm_password(self):
        """Cleans confirm password
        :return: str confirm password
        :raise forms.ValidationError: if both passwords are not equals
        """
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError(
                AppMessage.error['PASSWORD_MISMATCH']
            )
        return password

    def clean_email(self):
        """ Clean form email.
        :return str email: cleaned email
        :raise forms.ValidationError: Email is duplicated
        """
        # Since EmailUser.email is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.

        email = self.cleaned_data.get('email')
        try:
            get_user_model()._default_manager.get(email=email)
        except get_user_model().DoesNotExist:
            return email

        raise forms.ValidationError(
            AppMessage.error['DUPLICATE_EMAIL'],
            code='DUPLICATE_EMAIL',
        )

    def clean_zipcode(self):
        """ Cleans form zipcode
        :return int zipcode: cleaned zipcode
        :raise forms.ValidationError: zipcode max_length exceeds
        """
        zipcode = self.cleaned_data.get('zipcode')
        if not isinstance(zipcode, int):
            raise forms.ValidationError(
                AppMessage.error['ZIPCODE_NOT_INT']
            )
        elif not (len(str(zipcode)) == 5 or len(str(zipcode)) == 6):
            raise forms.ValidationError(
                AppMessage.error['ZIPCODE_LENGTH_INCORRECT']
            )
        return zipcode

    def clean_tnc(self):
        """
        Cleans terms and conditions
        :return: int tnc
        """
        tnc = self.cleaned_data.get('tnc')
        if not tnc:
            raise forms.ValidationError(AppMessage.error['SIGNUP_AGREE_TNC'])

        return tnc

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'zipcode', 'password',
                  'tnc']


class UserLoginForm(forms.Form):

    email = forms.EmailField(widget=forms.widgets.TextInput)
    password = forms.CharField(widget=forms.widgets.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email address'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError(AppMessage.error['PASSWORD_REQUIRED'])
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            get_user_model()._default_manager.get(email=email)
            return email
        except get_user_model().DoesNotExist:
            raise forms.ValidationError(AppMessage.error['LOGIN_FAILS'])

    class Meta:
        fields = ['email', 'password']


class UserForgotPasswordForm(forms.Form):

    email = forms.EmailField(widget=forms.widgets.TextInput)

    def __init__(self, *args, **kwargs):
        super(UserForgotPasswordForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'inut_bj'
        self.fields['email'].widget.attrs['placeholder'] = 'Email address'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            get_user_model()._default_manager.get(email=email)
            return email
        except get_user_model().DoesNotExist:
            raise forms.ValidationError(AppMessage.error['EMAIL_NOT_EXISTS'])

    class Meta:
        fields = ['email']


class UserResetPasswordForm(forms.Form):
    """
    A form for user signup.
    Includes fields first name, last name, email, password, tnc name zipcode
    """
    password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput
    )
    confirm_password = forms.CharField(
        label=_("Confirm Password"),
        widget=forms.PasswordInput
    )

    def __init__(self, *args, **kwargs):
        super(UserResetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = \
            'Enter your new password'
        self.fields['confirm_password'].widget.attrs['class'] = 'form-control'
        self.fields['confirm_password'].widget.attrs['placeholder'] = \
            'Re-enter your new password'

    def clean_password(self):
        """Cleans password
        :return: str password
        :raise forms.ValidationError: if password length is not correct.
        """
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise forms.ValidationError(
                AppMessage.error['PASSWORD_LENGTH_MIN']
            )
        elif len(password) > 30:
            raise forms.ValidationError(
                AppMessage.error['PASSWORD_LENGTH_MAX']
            )
        return password

    def clean_confirm_password(self):
        """Cleans confirm password
        :return: str confirm password
        :raise forms.ValidationError: if both passwords are not equals
        """
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError(
                AppMessage.error['PASSWORD_MISMATCH']
            )
        return password

    class Meta:
        fields = ['password', 'confirm_password']
