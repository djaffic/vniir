from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from departments.models import *
# Register your models here

class DepartmentAdmin(SummernoteModelAdmin):
    summernote_fields = ('text', 'science',)

admin.site.register(Department, DepartmentAdmin)

class ManagementAdmin(SummernoteModelAdmin):
    summernote_fields = ('biografy',)
    list_display = ('full_name', 'slug', 'id',)

admin.site.register(Management, ManagementAdmin)