from django.db import models
from custom_user.models import CustomUser
from contents.models import Department, Lab
from django.conf import settings

class Job(models.Model):
    user = models.ForeignKey(CustomUser, null=True, blank=True)
    lab = models.ForeignKey(Lab)
    # lab = models.ForeignKey(Lab, null=True, blank=True)

    open_date = models.DateTimeField()
    job_title = models.CharField(max_length=100)
    type = models.CharField(max_length=100, null=True, blank=True)
    temporary = models.BooleanField()
    hours_per_week = models.IntegerField()
    work_schedule_summary = models.TextField()
    work_study_job = models.BooleanField()
    department = models.ForeignKey(Department)
    pay_rate_range_min = models.DecimalField(max_digits=8, decimal_places=2)
    pay_rate_range_max = models.DecimalField(max_digits=8, decimal_places=2)
    pay_rate_currency_code = models.CharField(max_length=3, null=False, choices=settings.CURRENCY_CHOICES, default='USD')
    close_date = models.DateTimeField()
    job_summary = models.TextField()
    responsibilities = models.TextField()
    minimum_qualification = models.TextField()
    preferences = models.TextField(null=True, blank=True)
    additional_information = models.TextField(null=True, blank=True)
    is_paid = models.BooleanField()
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class PaymentInfo(models.Model):
    cm = models.CharField(primary_key=True, max_length=255)
    tx = models.CharField(max_length=255)
    cc = models.CharField(max_length=255)
    amt = models.CharField(max_length=255)
    item_number = models.CharField(max_length=255)
    st = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name