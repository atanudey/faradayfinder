from django.contrib import admin
from logs.models import Log


# Register your models here.
class LogAdmin(admin.ModelAdmin):
    list_display = ('log_type', 'name', 'description', 'added_on')

admin.site.register(Log, LogAdmin)
