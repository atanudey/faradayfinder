"""
User profile related views
"""

import json
import logging
from utils.common import AppMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.template import loader, RequestContext
from custom_user.forms import profile_forms
from custom_user.forms.upload_photo_forms import UploadProfilePhoto
from custom_user.models import CustomUser
from django.contrib import messages

LOGGING = logging.getLogger(__name__)


class UserChangePassword(View):
    template_name = 'o/change-password.html'
    form = profile_forms.EditPassword

    def get(self, request, *args, **kwargs):
        context = {
            'form': self.form()
        }
        template = loader.get_template(self.template_name)
        data = RequestContext(request, context)
        return HttpResponse(template.render(data))

    def post(self, request, *args, **kwargs):
        context = dict(result=False)
        status = 400

        if request.is_ajax():
            form_password = self.form(request.POST)
            if form_password.is_valid():
                LOGGING.debug('I am validated successfully..')
                password = request.POST.get('password')
                new_password = request.POST.get('new_password')

                if request.user.check_password(password):
                    request.user.set_password(new_password)
                    request.user.save()
                    status = 201
                    context['message'] = \
                        AppMessage.success['PASSWORD_CHANGED_SUCCESS']
                    context['result'] = True
                else:
                    context['message'] = \
                        AppMessage.error['PASSWORD_CHANGE_FAILED']
            else:
                context.update(form_password.errors)
        else:
            context['message'] = AppMessage.error['INVALID_REQUEST']
        return HttpResponse(content=json.dumps(context), status=status)


class UserEditNetwork(View):

    template_name = 'o/edit-network.html'
    form = profile_forms.EditNetwork

    def get(self, request, *args, **kwargs):

        data = {
            'is_phone_public': request.user.is_phone_public,
            'phone': request.user.phone,
            'is_facebook_public': request.user.is_facebook_public,
            'facebook': request.user.facebook,
            'is_linkedin_public': request.user.is_linkedin_public,
            'linkedin': request.user.linkedin,
            'is_skype_public': request.user.is_skype_public,
            'skype': request.user.skype,
            'is_twitter_public': request.user.is_twitter_public,
            'twitter': request.user.twitter,
            'is_aim_public': request.user.is_aim_public,
            'aim': request.user.aim,
            'photo': request.user.photo,
            'resume': request.user.resume
        }

        context = {
            'form': self.form(initial=data)
        }

        # taking flush messages
        load_message = messages.get_messages(request)
        for storage in load_message:
            context['flush_message'] = storage

        template = loader.get_template(self.template_name)
        data = RequestContext(request, context)
        return HttpResponse(template.render(data))

    def post(self, request, *args, **kwargs):
        context = dict(result=False)

        form = self.form(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                AppMessage.success['EDIT_NETWORK_SUCCESS']
            )
        else:
            context.update(form.errors)
        return HttpResponseRedirect('/accounts/edit-network/')

class UserEditProfile(View):

    template_name = 'o/edit-profile.html'
    form = profile_forms.EditProfileForm

    def get(self, request, *args, **kwargs):
        data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'dob': request.user.dob,
            'address': request.user.address,
            'city': request.user.city,
            'state': request.user.state,
            'country': request.user.country,
            'zipcode': request.user.zipcode,
            'about_me': request.user.about_me,
            'is_phone_public': request.user.is_phone_public,
            'phone': request.user.phone,
            'is_facebook_public': request.user.is_facebook_public,
            'facebook': request.user.facebook,
            'is_linkedin_public': request.user.is_linkedin_public,
            'linkedin': request.user.linkedin,
            'is_skype_public': request.user.is_skype_public,
            'skype': request.user.skype,
            'is_twitter_public': request.user.is_twitter_public,
            'twitter': request.user.twitter,
            'is_aim_public': request.user.is_aim_public,
            'aim': request.user.aim
        }

        context = {
            'form': self.form(initial=data)
        }
        template = loader.get_template(self.template_name)
        data = RequestContext(request, context)
        return HttpResponse(template.render(data))

    def post(self, request, *args, **kwargs):
        context = dict(result=False)
        status = 400

        if request.is_ajax():
            form = self.form(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                status = 200
                context['message'] = \
                    AppMessage.success['EDIT_NETWORK_SUCCESS']
                context['result'] = True
            else:
                context.update(form.errors)
        else:
            context['message'] = AppMessage.error['INVALID_REQUEST']
        return HttpResponse(content=json.dumps(context), status=status)

# class UserEditProfile(View):
#
#     template_name = 'edit-profile.html'
#     form = EditProfileForm
#     form_network = EditNetwork
#     form_password = EditPassword
#
#     def get(self, request, *args, **kwargs):
#         data = {
#             'first_name': request.user.first_name,
#             'last_name': request.user.last_name,
#             'dob': request.user.dob,
#             'address': request.user.address,
#             'city': request.user.city,
#             'state': request.user.state,
#             'country': request.user.country,
#             'zipcode': request.user.zipcode,
#             'about_me': request.user.about_me,
#             'is_phone_public': request.user.is_phone_public,
#             'phone': request.user.phone,
#             'is_facebook_public': request.user.is_facebook_public,
#             'facebook': request.user.facebook,
#             'is_linkedin_public': request.user.is_linkedin_public,
#             'linkedin': request.user.linkedin,
#             'is_skype_public': request.user.is_skype_public,
#             'skype': request.user.skype,
#             'is_twitter_public': request.user.is_twitter_public,
#             'twitter': request.user.twitter,
#             'is_aim_public': request.user.is_aim_public,
#             'aim': request.user.aim
#         }
#
#         context = {
#             'form_edit_profile': self.form(initial=data),
#             'form_edit_network': self.form_network(initial=data),
#             'form_edit_password': self.form_password()
#         }
#         template = loader.get_template(self.template_name)
#         data = RequestContext(request, context)
#         return HttpResponse(template.render(data))
#
#     def post(self, request, *args, **kwargs):
#         context = dict(result=False)
#         status = 400
#
#         if request.is_ajax():
#             # for edit profile
#             if 'first_name' in request.POST:
#                 form = self.form(request.POST, instance=request.user)
#                 if form.is_valid():
#                     form.save()
#                     status = 201
#                     context['message'] = \
#                         AppMessage.success['EDIT_PROFILE_SUCCESS']
#                     context['result'] = True
#                 else:
#                     context.update(form.errors)
#             # for edit network
#             elif 'phone' in request.POST:
#                 form_network = self.form_network(request.POST,
#                                                  instance=request.user
#                 )
#                 if form_network.is_valid():
#                     form_network.save()
#                     status = 201
#                     context['message'] = \
#                         AppMessage.success['EDIT_NETWORK_SUCCESS']
#                     context['result'] = True
#                 else:
#                     context.update(form_network.errors)
#             # for change password
#             elif 'password' in request.POST:
#                 form_password = self.form_password(request.POST)
#
#                 if form_password.is_valid():
#                     LOGGING.debug('I am validated successfully..')
#                     password = request.POST.get('password')
#                     new_password = request.POST.get('new_password')
#
#                     if request.user.check_password(password):
#                         request.user.set_password(new_password)
#                         request.user.save()
#                         status = 201
#                         context['message'] = \
#                             AppMessage.success['PASSWORD_CHANGED_SUCCESS']
#                         context['result'] = True
#                     else:
#                         context['message'] = \
#                             AppMessage.error['PASSWORD_CHANGE_FAILED']
#                 else:
#                     context.update(form_password.errors)
#         else:
#             context['message'] = AppMessage.error['INVALID_REQUEST']
#         return HttpResponse(content=json.dumps(context), status=status)


class UploadProfilePhoto(View):

    def post(self, request, *args, **kwargs):
        context = dict(result=False)
        status = 400
        LOGGING.debug('I am here')
        # form = UploadProfilePhoto(request.POST, request.FILES)
        # if form.is_valid():
        LOGGING.debug('I am here 2')
        photo = CustomUser(photo=request.FILES['file'])
        photo.save()
        context['result'] = True
        status = 200
        return HttpResponse(context)




