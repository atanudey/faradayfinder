from django import forms
from contents import models


class FormUpdateEquipment(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        instance = kwargs['instance']
        self.user = instance.user
        super(FormUpdateEquipment, self).__init__(*args, **kwargs)
        fields_name = ['name', 'photo', 'password', 'primary_url',
                       'primary_twitter', 'lab', 'is_private', 'password',
                       'latitude', 'longitude', 'description', 'meta_keyword',
                       'meta_abstract', 'meta_description', 'facebook',
                       'twitter', 'skype', 'phone', 'linkedin', 'email',
                       'video', 'paypal_account', 'address', 'city',
                       'state', 'country', 'zipcode']
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

    class Meta:
        model = models.Equipment
        exclude_fields = ['added_on', 'updated_on']


class FormEquipments(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(FormEquipments, self).__init__(*args, **kwargs)
        fields_name = ['name', 'photo', 'password', 'primary_url',
                       'primary_twitter', 'lab', 'is_private', 'password',
                       'latitude', 'longitude', 'description', 'meta_keyword',
                       'meta_abstract', 'meta_description', 'facebook',
                       'twitter', 'skype', 'phone', 'linkedin', 'email',
                       'video', 'paypal_account', 'address', 'city',
                       'state', 'country', 'zipcode']
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
                                        'to create your Equipment')
        return tnc

    def clean_user(self):
        return self.user

    def clean_password(self):
        password = self.cleaned_data.get('password', '').strip()
        is_private = self.cleaned_data.get('is_private')

        if is_private and not password:
            raise forms.ValidationError('Please enter a password since you '
                                        ' have selected your project as'
                                        ' password protected ')
        return password

    def clean_name(self):
        """
        If somebody enters into this form ' hello ',
        the extra whitespace will be stripped.
        """
        return self.cleaned_data.get('name', '').strip()

    class Meta:
        model = models.Equipment
        exclude_fields = ['added_on', 'updated_on']
