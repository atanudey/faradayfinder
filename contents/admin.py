from django.contrib import admin
from contents import models


# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'institute', 'order_number',
                    'is_deleted', 'added_on', 'updated_on')


# Register your models here.
class InstituteAdmin(admin.ModelAdmin):
    list_display = ('name', 'order_number', 'is_deleted',
                    'added_on', 'updated_on')


# Register your models here.
class LabAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'institute', 'department',
                    'is_deleted', 'added_on', 'updated_on')


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'lab', 'is_deleted',
                    'added_on', 'updated_on')


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'lab', 'event_date', 'is_deleted',
                    'added_on', 'updated_on')


# Register your models here.
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'lab', 'is_deleted',
                    'added_on', 'updated_on')


admin.site.register(models.Lab, LabAdmin)
admin.site.register(models.Institute, InstituteAdmin)
admin.site.register(models.Department, DepartmentAdmin)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Equipment, EquipmentAdmin)