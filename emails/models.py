from django.db import models


# Create your models here.
class Email(models.Model):

    to = models.EmailField(max_length=200)
    from_email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}-{}' . format(self.to, self.subject)
