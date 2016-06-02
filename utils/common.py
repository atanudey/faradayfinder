"""
Defines common util function for the application
"""

import random
import string
import base64
import logging
from django.core.mail import send_mail
from django.conf import settings
from utils.exception import AppMessage
from django.template import loader, RequestContext
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from emails.views import log_email
from logs.views import logs

LOGGER = logging.getLogger(__name__)


def random_number(length=32):
    """ Returns a random number
    :param length: int
    :return: string: return a string
    """
    return ''.join([random.choice(string.ascii_letters + string.digits)
                    for data in range(length)])


def encode(val):
    """
    encodes a value
    :param val: string
    :return: string
    """
    return base64.b64encode(bytes(val, encoding='utf-8'))


def decode(val):
    """
    decodes a value
    :param val: string
    :return: string
    """
    return base64.b64decode(val).decode('utf-8')


def anonymous_required(func):
    def as_view(request, *args, **kwargs):
        # redirect_to = kwargs.get('next', settings.LOGIN_REDIRECT_URL )
        LOGGER.info('GET QUERY PARAM')
        LOGGER.info(request.GET)
        LOGGER.info('GET POST PARAM')
        LOGGER.info(request.POST)
        redirect_to = kwargs.get('next', '')
        if redirect_to == '':
            if request.method == 'GET':
                redirect_to = request.GET.get(
                    'next', settings.LOGIN_REDIRECT_URL)
            elif request.method == 'POST':
                redirect_to = request.POST.get(
                    'next', settings.LOGIN_REDIRECT_URL)

        LOGGER.info('Before authentication check Redirecting to {}'.format(redirect_to))
        if request.user.is_authenticated():
            return HttpResponseRedirect(redirect_to)
        response = func(request, *args, **kwargs)
        return response
    return as_view


class Email():
    """
    Email class will be used to send email
    """
    @staticmethod
    def go_email(**kwargs):
        try:
            to = kwargs['to']
            from_email = kwargs['from_email']
            subject = kwargs['subject']
            message = kwargs['message']
            log_email(to, from_email, subject, message)
            LOGGER.info('Trying to send email')
            send_mail(subject, message, from_email, [to])
            LOGGER.info('Email sent successful')
            logs(log_type='info',
                 name='Email sending successful',
                 description='Email Successful, to: {}, '
                             'from_email: {}, '
                             'subject: {}, message: {}' .
                 format(to, from_email, subject, message))
        except Exception as e:
            LOGGER.error('Email sending failed for {}' . format(to))
            logs(log_type='danger',
                 name='Email sending failed for- {}, '
                      'to-{}' . format(subject, to),
                 description='Email failed, to: {}, '
                             'from_email: {}, '
                             'subject: {}, message: {}, e= {}' .
                 format(to, from_email, subject, message, str(e)))
            raise Exception(AppMessage.error['EMAIL_SENDING_FAIL'])


class LoginUser(object):

    def __init__(self, request, user):
        self.user = user
        self.request = request

    def go_login(self, email, password=None):
        if not password:
            self.user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(self.request, self.user)
        else:
            u = authenticate(email=email, password=password)
            login(self.request, u)


def template_path():
    return 'o/'
