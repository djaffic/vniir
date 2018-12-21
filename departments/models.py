from django.db import models
from django.shortcuts import reverse
from django.db.models import Q


class DepartmentManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query) |
                         Q(text__icontains=query) |
                         Q(science__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs

def image_folder(instance, filename):
    filename = instance.slug + "." + filename.split(".")[1]
    return "department/{0}/{1}".format(instance.slug, filename)

class Department(models.Model):
    title = models.CharField(verbose_name="Название отдела", max_length=200, blank=False)
    short_title = models.CharField(verbose_name="Короткое название", max_length=6, blank=False, null=True)
    slug = models.SlugField(verbose_name="Ссылка на отдел", unique=True, blank=False)
    image = models.ImageField(verbose_name="Картинка отдела", upload_to=image_folder, blank=True)
    text = models.TextField(verbose_name="Услуги отдела", blank=True)
    science = models.TextField(verbose_name="Научная деятельность", blank=True)
    email = models.EmailField(verbose_name="Email", max_length=200, blank=True)
    phone = models.CharField(verbose_name="Телефон", blank=False, max_length=50)
    head_of_department = models.CharField(verbose_name="Начальник отдела", max_length=200)

    objects = DepartmentManager()

    class Meta:
        verbose_name="Отдел"
        verbose_name_plural="Отделы"

    def get_absolute_url(self):
        return reverse('department_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


def image_folder(instance, filename):
    filename = instance.slug + "." + filename.split(".")[1]
    return "management/{0}/{1}".format(instance.slug, filename)


class ManagementManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(full_name__icontains=query) |
                         Q(text__icontains=query) |
                         Q(biografy__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
        return qs


class Management(models.Model):
    full_name = models.CharField(verbose_name="Полное имя", max_length=200)
    slug = models.SlugField(verbose_name="Ссылка", unique=True)
    image = models.ImageField(upload_to=image_folder)
    position = models.CharField(verbose_name="Занимаемая должность", max_length=200)
    text = models.TextField(verbose_name="д.т.н. и т.д.", blank=True)
    biografy = models.TextField(verbose_name="Биография", blank=True)

    objects = ManagementManager()

    class Meta:
        verbose_name = "Руководство"
        verbose_name_plural = "Руководство"

    def get_absolute_url(self):
        return reverse('management_detail_url', kwargs={"slug": self.slug})

    def __str__(self):
        return self.full_name
