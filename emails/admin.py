from django.contrib import admin
from emails.models import Email


# Register your models here.
class EmailAdmin(admin.ModelAdmin):
    list_display = ('to', 'from_email', 'subject', 'message', 'added_on')

admin.site.register(Email, EmailAdmin)
