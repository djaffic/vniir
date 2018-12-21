from django.contrib import admin
from .models import Page, File
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class PageAdmin(SummernoteModelAdmin):
    summernote_fields = ("text",)

admin.site.register(Page, PageAdmin)
admin.site.register(File)