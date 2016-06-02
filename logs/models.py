from django.db import models


# Create your models here.
class Log(models.Model):

    CHOICES = (
        ('notice', 'notice'),
        ('info', 'info'),
        ('debug', 'debug'),
        ('warning', 'warning'),
        ('error', 'error'),
        ('danger', 'danger'),
    )
    log_type = models.CharField(
        choices=CHOICES, default='debug', max_length=20
    )
    name = models.TextField(null=True, blank=True)
    description = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}-{}- {}' . format(self.log_type, self.name, self.description)
