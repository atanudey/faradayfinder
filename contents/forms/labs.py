from django import forms
from contents.models import Lab
from utils.common import AppMessage


class FormUpdateLabs(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        instance = kwargs['instance']
        self.user = instance.user
        super(FormUpdateLabs, self).__init__(*args, **kwargs)

        fields_name = ['name', 'photo', 'password', 'primary_url',
                       'primary_twitter', 'institute','department',
                       'is_private', 'password', 'address', 'city', 'state',
                       'country', 'zipcode', 'latitude', 'longitude',
                       'description', 'meta_keyword', 'meta_abstract',
                       'meta_description', 'facebook', 'twitter', 'skype',
                       'phone', 'linkedin', 'email', 'video', 'paypal_account']
        for field in fields_name:
            self.fields[field].widget.attrs['class'] = 'input_bg'

        self.fields['description'].widget.attrs['style'] = \
            'width:591px; height:100px;'
        self.fields['meta_keyword'].widget.attrs['style'] = \
            'width:591px; height:50px;'
        self.fields['meta_abstract'].widget.attrs['style'] = \
            'width:591px; height:50px;'
        self.fields['meta_description'].widget.attrs['style'] = \
            'width:591px; height:100px;'

    def clean_user(self):
        return self.user

    def clean_password(self):
        password = self.cleaned_data.get('password', '').strip()
        is_private = self.cleaned_data.get('is_private')

        if is_private and not password:
            raise forms.ValidationError('Please enter a password since you '
                                        ' have selected your lab as'
                                        ' password protected ')
        return password

    def clean_name(self):
        """
        If somebody enters into this form ' hello ',
        the extra whitespace will be stripped.
        """
        return self.cleaned_data.get('name', '').strip()

    def clean_zipcode(self):
        """ Cleans form zipcode
        :return int zipcode: cleaned zipcode
        :raise forms.ValidationError: zipcode max_length exceeds
        """
        zipcode = self.cleaned_data.get('zipcode')
        if not (len(str(zipcode)) == 5 or len(str(zipcode)) == 6):
            raise forms.ValidationError(
                AppMessage.error['ZIPCODE_LENGTH_INCORRECT']
            )
        return zipcode

    class Meta:
        model = Lab
        exclude_fields = ['added_on', 'updated_on']


class FormLabs(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(FormLabs, self).__init__(*args, **kwargs)
        fields_name = ['name', 'photo', 'password', 'primary_url',
                       'primary_twitter', 'institute','department',
                       'is_private', 'password', 'address', 'city', 'state',
                       'country', 'zipcode', 'latitude', 'longitude',
                       'description', 'meta_keyword', 'meta_abstract',
                       'meta_description', 'facebook', 'twitter', 'skype',
                       'phone', 'linkedin', 'email', 'video', 'paypal_account']
        for field in fields_name:
            self.fields[field].widget.attrs['class'] = 'input_bg'

        self.fields['description'].widget.attrs['style'] = \
            'width:591px; height:100px;'
        self.fields['meta_keyword'].widget.attrs['style'] = \
            'width:591px; height:50px;'
        self.fields['meta_abstract'].widget.attrs['style'] = \
            'width:591px; height:50px;'
        self.fields['meta_description'].widget.attrs['style'] = \
            'width:591px; height:100px;'

    def clean_tnc(self):
        tnc = self.cleaned_data.get('tnc')
        if not tnc:
            raise forms.ValidationError('Please agree with Terms and '
                                        'Conditions of FaradayFinder.com '
                                        'to create your Lab')
        return tnc

    def clean_user(self):
        return self.user

    def clean_password(self):
        password = self.cleaned_data.get('password', '').strip()
        is_private = self.cleaned_data.get('is_private')

        if is_private and not password:
            raise forms.ValidationError('Please enter a password since you '
                                        ' have selected your lab as'
                                        ' password protected ')
        return password

    def clean_name(self):
        """
        If somebody enters into this form ' hello ',
        the extra whitespace will be stripped.
        """
        return self.cleaned_data.get('name', '').strip()

    def clean_zipcode(self):
        """ Cleans form zipcode
        :return int zipcode: cleaned zipcode
        :raise forms.ValidationError: zipcode max_length exceeds
        """
        zipcode = self.cleaned_data.get('zipcode')
        if not (len(str(zipcode)) == 5 or len(str(zipcode)) == 6):
            raise forms.ValidationError(
                AppMessage.error['ZIPCODE_LENGTH_INCORRECT']
            )
        return zipcode


    class Meta:
        model = Lab
        exclude_fields = ['added_on', 'updated_on']
