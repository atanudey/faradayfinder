""" Views for custom user. """

import json
from django.core.serializers.json import DjangoJSONEncoder
import logging
from utils import common
from custom_user.models import CustomUser
from django.conf import settings
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth import logout
from utils.exception import AppMessage
from utils.common import Email, LoginUser
from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from custom_user.forms.account_forms import UserSignup, UserLoginForm, \
    UserForgotPasswordForm, UserResetPasswordForm
from django.db.models import Q

LOGGER = logging.getLogger(__name__)

class UsersMessage(View):    
    def get(self, request, *args, **kwargs):
        context = dict(result=False)
        status = 400
        
        if request.is_ajax():
            term = request.GET.get('term')        
            sort_by = "first_name"            
            if term != "":
                filter_fn = 'first_name__icontains'
                filter_ln = 'last_name__icontains'
                filter_email = 'email__icontains'
                user_set = CustomUser.objects.filter(Q(first_name__icontains = term) | Q(last_name__icontains = term) | Q(email__icontains = term), is_active=True)
            else:
                user_set = CustomUser.objects.filter(is_active=True)
                
            user_set = user_set.order_by(sort_by)
            
            users = []        
            for user in user_set:
                user_info = {}
                user_info["id"] = user.email            
                user_info["name"] = user.first_name + " " + user.last_name + " [" + user.email + "]"
                users.append(user_info)       
            
            return HttpResponse(json.dumps(users), content_type="application/json")
        else:
            context['message'] = AppMessage.error['INVALID_REQUEST']
            return HttpResponse(content=json.dumps(context), status=status)

class GetUserById(View):
    def get(self, request, *args, **kwargs):
        context = dict(result=False)
        status = 400
        
        #if request.is_ajax():
        uid = int(request.GET.get('uid'))
        if uid > 0:                
            user_set = CustomUser.objects.filter(pk=uid).values('last_login','is_superuser','first_name','last_name','email','zipcode','is_staff','is_active','date_joined','date_updated','about_me','verify_number','tnc','dob','address','city','state','country_id','is_phone_public','phone','is_facebook_public','facebook','is_linkedin_public','linkedin','is_skype_public','skype','is_twitter_public','twitter','is_aim_public','aim','photo','resume')                       
            return HttpResponse(json.dumps(list(user_set), cls=DjangoJSONEncoder), content_type="application/json")
        #else:
            #context['message'] = AppMessage.error['INVALID_REQUEST']
            #return HttpResponse(content=json.dumps(context), status=status)

class UserResetPassword(View):
    template_name = 'o/reset-password.html'
    form = UserResetPasswordForm

    @staticmethod
    def confirm_verify_number(request, *args, **kwargs):
        verify_number = kwargs.get('verify_number')
        try:
            user = CustomUser.objects.\
                get(is_active=True, verify_number=verify_number)
            return user
        except Exception as e:
            LOGGER.debug(str(e))
        return False

    def get(self, request, *args, **kwargs):
        context = {'form': self.form(initial=None)}
        if not self.confirm_verify_number(request, *args, **kwargs):
            context['flush_message'] = \
                AppMessage.error['INCORRECT_ACTIVATION_LINK']
        load_message = messages.get_messages(request)
        for storage in load_message:
            context['flush_message'] = storage
        template = loader.get_template(self.template_name)
        data = RequestContext(request, context)
        return HttpResponse(template.render(data))

    def post(self, request, *args, **kwargs):
        context = dict(result=False)
        status = 400

        if request.is_ajax():
            form = self.form(request.POST)
            if form.is_valid():
                try:
                    user = self.confirm_verify_number(request, *args, **kwargs)
                    if user:
                        user.set_password(request.POST.get('password'))
                        user.verify_number = common.random_number()
                        user.save()

                        status = 201
                        context['result'] = True
                        context['next_page'] = '/accounts/login'
                        messages.success(
                            request,
                            AppMessage.success['RESET_PASSWORD_SUCCESS']
                        )
                    else:
                        context['message'] = \
                            AppMessage.error['FORGOT_PASSWORD_REQUEST_FAIL']
                except Exception as e:
                    LOGGER.debug(str(e))
                    context['message'] = \
                        AppMessage.error['FORGOT_PASSWORD_REQUEST_FAIL']
            else:
                context.update(form.errors)
        else:
            context['message'] = AppMessage.error['INVALID_REQUEST']
        return HttpResponse(content=json.dumps(context), status=status)


class UserForgotPassword(View):
    """This class is used to reset password for a user."""

    template_name = 'o/forgot-password.html'
    form = UserForgotPasswordForm

    def get(self, request, *args, **kwargs):
        """
        Renders forgot password page to user. User can enter his email
        address a send a request to reset password
        """
        context = {'form': self.form(initial=None)}
        template = loader.get_template(self.template_name)
        data = RequestContext(request, context)
        return HttpResponse(template.render(data))

    def post(self, request, *args, **kwargs):
        context = dict(result=False)
        status = 400

        if request.is_ajax():
            form = self.form(request.POST)
            if form.is_valid():
                try:
                    verify_number = common.random_number()
                    email = request.POST.get('email')
                    user = CustomUser.objects.get(email=email, is_active=True)
                    user.verify_number = verify_number
                    user.save()

                    # sending email
                    # signup email template
                    template = loader.get_template(
                        'emails/forgot-password.html'
                    )
                    message = template.render(
                        RequestContext(
                            request,
                            {
                                'first_name': user.first_name,
                                'website_url': settings.WEBSITE_URL,
                                'verify_number': verify_number
                            }
                        )
                    )

                    email_data = {
                        'to': email,
                        'from_email': settings.SUPPORT_EMAIL,
                        'subject': AppMessage.info[
                            'FORGOT_PASSWORD_EMAIL_SUBJECT'],
                        'message': message
                    }

                    # call to send email
                    try:
                        Email.go_email(**email_data)
                    except Exception as e:
                        LOGGER.debug(str(e))

                    status = 200
                    context['result'] = True
                    context['message'] = \
                        AppMessage.success['FORGOT_PASSWORD_REQUEST_SUCCESS']
                except Exception as e:
                    LOGGER.error(str(e))
                    context['message'] = \
                        AppMessage.error['FORGOT_PASSWORD_REQUEST_FAIL']
            else:
                context.update(form.errors)
        else:
            context['message'] = AppMessage.error['INVALID_REQUEST']
        return HttpResponse(content=json.dumps(context), status=status)


class UserLogout(View):
    """This class is used to make a user logout."""

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)


class UserLogin(View):

    template_name = 'o/login.html'
    login_form = UserLoginForm

    def get(self, request, *args, **kwargs):
        """
        This method renders login page to end user.
        """
        context = {'form': self.login_form(initial=None)}
        if '' != request.GET.get('next', ''):
            context['next'] = request.GET.get('next', '')
        load_message = messages.get_messages(request)
        for storage in load_message:
            context['flush_message'] = storage
        template = loader.get_template(self.template_name)
        data = RequestContext(request, context)
        return HttpResponse(template.render(data))

    def post(self, request, *args, **kwargs):
        """
        Accepts post request to login a user.
        It will accept email and password as input data and will validate it
        and user will authenticate if provides correct credentials.
        """
        context = dict(result=False)
        status = 400

        if request.is_ajax():
            form = self.login_form(request.POST)
            if form.is_valid():
                try:
                    email = request.POST.get('email')
                    password = request.POST.get('password')
                    user = CustomUser.objects.get(email=email, is_active=True)

                    # login
                    login_user = LoginUser(request, user)
                    login_user.go_login(email, password)

                    if request.user.is_authenticated():
                        context['next_page'] = request.POST.\
                            get('next', settings.LOGIN_REDIRECT_URL)
                        context['result'] = True
                        status = 200
                except Exception as e:
                    LOGGER.debug(str(e))
                    context['message'] = AppMessage.error['LOGIN_FAILS']
            else:
                context.update(form.errors)
        else:
            context['message'] = AppMessage.error['INVALID_REQUEST']
        return HttpResponse(content=json.dumps(context), status=status)


class UserAccountActivate(View):
    """This class is used to activate a user accounts after registration.
    If activation link is correct then user will be logged in and will
    be redirected to his account/profile page."""

    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        """
        Checked verify number. If it is correct then will call login
        otherwise 400 response.
        """
        try:
            user = CustomUser.objects.\
                get(is_active=False, verify_number=kwargs['verify_number'])
            # login
            login_user = LoginUser(request, user)
            login_user.go_login(user.email, None)
            logging.info('I am here ')

            if request.user.is_authenticated():
                user.is_active = True
                user.save()
                # messages.add_message(
                #     request, messages.SUCCESS,
                #     'Thank you for activation of your account.'
                # )
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        except Exception as e:
            messages.add_message(request, messages.ERROR,
                                 AppMessage.error['INCORRECT_ACTIVATION_LINK'])
            LOGGER.debug(str(e))
        return HttpResponseRedirect('/accounts/login/')


class UserSignup(View):
    """This class is used to register a user. After successfully registeration
    user will get one email to activate account."""

    signup_form = UserSignup
    template_name = 'o/signup.html'

    def get(self, request, *args, **kwargs):
        """
        signup form get method.
        """
        context = {'form': self.signup_form(initial=None)}
        template = loader.get_template(self.template_name)
        data = RequestContext(request, context)
        return HttpResponse(template.render(data))

    def post(self, request, *args, **kwargs):
        """
        signup form post method
        """
        context = dict(result=False)
        status = 400
        if request.is_ajax():
            form = self.signup_form(request.POST)

            LOGGER.debug(request.POST)

            if form.is_valid():
                try:
                    verify_number = common.random_number()
                    data = dict(
                        first_name=request.POST.get('first_name'),
                        last_name=request.POST.get('last_name'),
                        zipcode=request.POST.get('zipcode'),
                        tnc=request.POST.get('tnc'),
                        is_active=False,
                        verify_number=verify_number
                    )

                    # creates a new user
                    CustomUser.objects.create_user(
                        request.POST['email'],
                        request.POST['password'],
                        **data
                    )

                    # signup email template
                    template = loader.get_template('emails/signup.html')
                    message = template.render(
                        RequestContext(
                            request,
                            {
                                'first_name': request.POST['first_name'],
                                'website_url': settings.WEBSITE_URL,
                                'verify_number': verify_number
                            }
                        )
                    )

                    # sending email
                    email_data = {
                        'to': request.POST['email'],
                        'from_email': settings.SUPPORT_EMAIL,
                        'subject': AppMessage.info['SIGNUP_EMAIL_SUBJECT'],
                        'message': message
                    }
                    try:
                        # call to send email
                        Email.go_email(**email_data)
                    except Exception as e:
                        LOGGER.debug(str(e))

                    context['result'] = True
                    context['message'] = AppMessage.success['SIGNUP_SUCCESS']
                    status = 201
                except Exception as e:
                    LOGGER.debug(str(e))
                    context['message'] = AppMessage.error['SIGNUP_FAILS']
            else:
                context.update(form.errors)
        else:
            context['message'] = AppMessage.error['INVALID_REQUEST']
        return HttpResponse(content=json.dumps(context), status=status)
