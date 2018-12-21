from django.db import models
from django.shortcuts import reverse


class Standarts_Type(models.Model):
    title = models.CharField(verbose_name="Тип эталона", max_length=200)
    slug = models.SlugField(verbose_name="Ссылка на тип эталона", blank=True)

    class Meta:
        verbose_name = "Тип эталона"
        verbose_name_plural = "Типы эталонов"

    def get_absolute_url(self):
        return reverse("standards_type_detail_url", kwargs={'slug':self.slug})

    def __str__(self):
        return self.title


class StandardManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query) |
                         Q(text__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
        return qs


class Standard(models.Model):
    title = models.CharField(verbose_name="Название эталона", max_length=200)
    slug = models.SlugField(verbose_name="Ссылка на эталон", blank=True)
    text = models.TextField(verbose_name="Описание эталона")
    standards_type = models.ForeignKey(Standarts_Type, verbose_name="Тип эталона", null=True, on_delete=models.SET_NULL)
    # type = models.ForeignKey(Standarts_Type, verbose_name="Тип эталона", null=True, on_delete=models.SET_NULL)
    objects = StandardManager()
    class Meta:
        verbose_name = "Эталон"
        verbose_name_plural = "Эталоны"

    def get_absolute_url(self):
        return reverse("standard_detail_url", kwargs={'slug':self.slug})

    def __str__(self):
        return self.title

