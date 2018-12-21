from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from articles.models import Tag, Article, Partner

#Регистрируем модели в админке
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Partner)
