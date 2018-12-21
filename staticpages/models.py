from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="Название страницы", max_length=50)
    text = models.TextField(verbose_name="Текст страницы", blank=True)
    slug = models.SlugField(unique=True, verbose_name="URL", blank=True)
    category = models.CharField(verbose_name="Категория страницы", max_length=20, null=True)

    class Meta:
        verbose_name = "Статическая страница"
        verbose_name_plural = "Статические страницы"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("get_page_url", kwargs={"slug":self.slug})


def filename(instance, filename):
    filename = instance.slug + "." + filename.split(".")[1]
    return "doc_files/{0}/{1}".format(instance.slug, filename)

class File(models.Model):
    page = models.ForeignKey(Page, verbose_name="Страница документов", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Название файла", max_length=200)
    file = models.FileField(upload_to=filename)
    slug = models.SlugField(max_length=200, verbose_name="URL to file", unique=True, blank=True)

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("get_file_url", kwargs={"slug": self.slug})