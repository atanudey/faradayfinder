""" Form Upload photo forms. """

import logging
from django import forms

LOGGER = logging.getLogger(__name__)


class UploadProfilePhoto(forms.Form):

    """
    This form is used to upload profile photo of user
    """
    #image = image.Image
    photo = forms.ImageField()
