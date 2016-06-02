# """
# To test activate account functions
# """
# import json
# import logging
# from django.test import TestCase, Client
# from custom_user.models import CustomUser
# from django.http import HttpRequest
# from django.contrib import messages
#
# LOGGER = logging.getLogger(__name__)
#
#
# class TestActivateAccount(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#         self.url = '/accounts/activate/verify/'
#
#     def tearDown(self):
#         CustomUser.objects.all().delete()
#
#     def test_with_invalid_activation_link(self):
#         request = HttpRequest()
#         response = self.client.get(self.url + 'test')
#         LOGGER.debug(dir(response))
#         LOGGER.debug(dir(response.streaming))
#         LOGGER.debug('3111212231132131313212')
#         storage = messages.get_messages(request)
#         LOGGER.debug(storage)
#
#
#         # response = json.loads(request.content.decode())
#         # LOGGER.debug(response)
#         assert False
#
#
#
#
#
#
#
