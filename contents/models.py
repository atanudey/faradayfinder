from django.db import models
from custom_user.models import CustomUser
from custom_user.models import Country

BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))


class Institute(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    order_number = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255)
    institute = models.ForeignKey(Institute, null=True, blank=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    order_number = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Lab(models.Model):
    name = models.CharField(max_length=255)
    # photo = models.ImageField(
    #     upload_to='/media/labs/', height_field=120, width_field=120,
    #     null=True, blank=True
    # )
    photo = models.ImageField(
        upload_to='labs/%Y/%m/'
    )
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(CustomUser, null=True, blank=True)
    institute = models.ForeignKey(Institute)
    department = models.ForeignKey(Department)
    primary_url = models.URLField(blank=True, null=True)
    primary_twitter = models.URLField(blank=True, null=True)
    is_private = models.BooleanField(default=False, choices=BOOL_CHOICES)
    password = models.CharField(max_length=50, null=True, blank=True)
    meta_keyword = models.CharField(max_length=200, null=True, blank=True)
    meta_abstract = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.ForeignKey(Country)
    zipcode = models.CharField(max_length=6)
    latitude = models.CharField(max_length=20, null=True, blank=True)
    longitude = models.CharField(max_length=20, null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    skype = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    video = models.TextField(null=True, blank=True)
    paypal_account = models.EmailField(null=True, blank=True)
    tnc = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class LabMember(models.Model):

    lab = models.ForeignKey(Lab)
    user = models.ForeignKey(CustomUser)
    added_on = models.DateTimeField(auto_now_add=True)


class Project(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='projects/%Y/%m/')
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(CustomUser, null=True, blank=True)
    lab = models.ForeignKey(Lab, null=True, blank=True)
    primary_url = models.URLField(blank=True, null=True)
    primary_twitter = models.URLField(blank=True, null=True)
    is_private = models.BooleanField(default=False, choices=BOOL_CHOICES)
    password = models.CharField(max_length=50, null=True, blank=True)
    meta_keyword = models.CharField(max_length=200, null=True, blank=True)
    meta_abstract = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.ForeignKey(Country)
    zipcode = models.CharField(max_length=6)
    latitude = models.CharField(max_length=20, null=True, blank=True)
    longitude = models.CharField(max_length=20, null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    skype = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    video = models.TextField(null=True, blank=True)
    paypal_account = models.EmailField(null=True, blank=True)
    tnc = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='events/%Y/%m/')
    user = models.ForeignKey(CustomUser, null=True, blank=True)
    lab = models.ForeignKey(Lab)
    event_date = models.DateTimeField()
    description = models.TextField(null=True, blank=True)
    primary_url = models.URLField(blank=True, null=True)
    primary_twitter = models.URLField(blank=True, null=True)
    is_private = models.BooleanField(default=False, choices=BOOL_CHOICES)
    password = models.CharField(max_length=50, null=True, blank=True)
    meta_keyword = models.CharField(max_length=200, null=True, blank=True)
    meta_abstract = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.ForeignKey(Country)
    zipcode = models.CharField(max_length=6)
    latitude = models.CharField(max_length=20, null=True, blank=True)
    longitude = models.CharField(max_length=20, null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    skype = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    video = models.TextField(null=True, blank=True)
    paypal_account = models.EmailField(null=True, blank=True)
    tnc = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='equipments/%Y/%m/')
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(CustomUser, null=True, blank=True)
    lab = models.ForeignKey(Lab)
    primary_url = models.URLField(blank=True, null=True)
    primary_twitter = models.URLField(blank=True, null=True)
    is_private = models.BooleanField(default=False, choices=BOOL_CHOICES)
    password = models.CharField(max_length=50, null=True, blank=True)
    meta_keyword = models.CharField(max_length=200, null=True, blank=True)
    meta_abstract = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.ForeignKey(Country)
    zipcode = models.CharField(max_length=6)
    latitude = models.CharField(max_length=20, null=True, blank=True)
    longitude = models.CharField(max_length=20, null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    skype = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    video = models.TextField(null=True, blank=True)
    paypal_account = models.EmailField(null=True, blank=True)
    tnc = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class ChatMessages(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='chatmessages_sender')
    sender_name = models.CharField(max_length=255)
    sender_email = models.EmailField(null=True, blank=True)
    receiver = models.ForeignKey(CustomUser, related_name='chatmessages_receiver')
    receiver_name = models.CharField(max_length=255)
    receiver_email = models.EmailField(null=True, blank=True)
    message = models.CharField(max_length=255)
    in_conversation = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
