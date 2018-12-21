from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *

# Register your models here.
class StandardAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)

admin.site.register(Standard, StandardAdmin)
admin.site.register(Standarts_Type)