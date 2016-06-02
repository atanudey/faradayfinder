""" User models."""
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Country(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):

    """ Custom manager for EmailUser."""

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """ Create and save an EmailUser with the given email and password.
        :param str email: user email
        :param str password: user password
        :param bool is_staff: whether user staff or not
        :param bool is_superuser: whether user admin or not
        :return custom_user.models.EmailUser user: user
        :raise ValueError: email is not set
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        is_active = extra_fields.pop("is_active", True)
        user = self.model(email=email, is_staff=is_staff, is_active=is_active,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """ Create and save an EmailUser with the given email and password.
        :param str email: user email
        :param str password: user password
        :return custom_user.models.EmailUser user: regular user
        """
        is_staff = extra_fields.pop("is_staff", False)
        return self._create_user(email, password, is_staff, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """ Create and save an EmailUser with the given email and password.
        :param str email: user email
        :param str password: user password
        :return custom_user.models.EmailUser user: admin user
        """
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class AbstractUser(AbstractBaseUser, PermissionsMixin):

    """ Abstract User with the same behaviour as Django's default User.
    AbstractEmailUser does not have username field. Uses email as the
    USERNAME_FIELD for authentication.
    Use this if you need to extend EmailUser.
    Inherits from both the AbstractBaseUser and PermissionMixin.
    The following attributes are inherited from the superclasses:
        * password
        * last_login
        * is_superuser
    """
    BOOL_CHOICES = ((True, 'Public'), (False, 'Private'))

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(_('email address'), max_length=255,
                              unique=True, db_index=True)
    zipcode = models.PositiveIntegerField(max_length=6, default=000000)
    tnc = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        _('staff status'), default=False, help_text=_(
            'Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=False, help_text=_(
        'Designates whether this user should be treated as '
        'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    about_me = models.TextField(null=True, blank=True)
    verify_number = models.CharField(
        max_length=32, default=None, blank=True, null=True
    )

    dob = models.DateField(blank=True, null=True, default=None)
    address = models.CharField(blank=True, null=True, max_length=50)
    city = models.CharField(blank=True, null=True, max_length=50)
    state = models.CharField(blank=True, null=True, max_length=50)
    country = models.ForeignKey(Country, default='United States')

    is_phone_public	= models.BooleanField(default=False, choices=BOOL_CHOICES)
    phone = models.CharField(blank=True, null=True, max_length=15)
    is_facebook_public = models.BooleanField(
        default=False, choices=BOOL_CHOICES
    )
    facebook = models.CharField(blank=True, null=True, max_length=200)
    is_linkedin_public = models.BooleanField(
        default=False, choices=BOOL_CHOICES
    )
    linkedin = models.CharField(blank=True, null=True, max_length=200)
    is_skype_public	= models.BooleanField(
        default=False, choices=BOOL_CHOICES
    )
    skype = models.CharField(blank=True, null=True, max_length=50)
    is_twitter_public = models.BooleanField(
        default=False, choices=BOOL_CHOICES
    )
    twitter = models.CharField(blank=True, null=True, max_length=200)
    is_aim_public = models.BooleanField(
        default=False, choices=BOOL_CHOICES
    )
    aim = models.CharField(blank=True, null=True, max_length=200)

    photo = models.ImageField(
        default=None,
        blank=True,
        null=True,
        upload_to='profile/%Y/%m/',
    )

    resume = models.FileField(
        default=None,
        blank=True,
        null=True,
        upload_to='resume/%Y/%m/',
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    def get_full_name(self):
        """ Return the full name."""
        return '{} {}' . format(self.first_name, self.last_name)

    def get_short_name(self):
        """ Return the first name."""
        return self.first_name
    
    def get_email(self):
        """ Return the email."""
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        """ Send an email to this User."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class CustomUser(AbstractUser):

    """
    Concrete class of AbstractEmailUser.
    Use this if you don't need to extend EmailUser.
    """

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
