from django.db import models
from django.shortcuts import reverse
from django.db.models import Q


class Tag(models.Model):
    #создаем модель тег для новости
    title = models.CharField(verbose_name="Название тега", max_length=30)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'pk': self.id})

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.title

def article_image_folder(instance, filename):
    filename = str(instance.id) + "." + filename.split(".")[1]
    return "articles/{0}/{1}".format(instance.id, filename)


class ArticleManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query) |
                         Q(text__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
        return qs


class Article(models.Model):
    #создаем модель новости
    title = models.CharField("Название статьи", max_length=200)
    text = models.TextField("Текст статьи")
    pub_date = models.DateField("Дата добавления", auto_now_add=False)
    tags = models.ManyToManyField(Tag, verbose_name="Теги")
    image = models.ImageField("Картинка статьи", upload_to=article_image_folder, blank=True)

    objects = ArticleManager()

    def get_absolute_url(self):
        return reverse('article_detail_url', kwargs={'pk': self.id})

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title


def image_folder(instance, filename):
    filename = instance.slug + "." + filename.split(".")[1]
    return "partners/{0}/{1}".format(instance.slug, filename)


class Partner(models.Model):
    #создаем модель партнера
    full_name = models.CharField(max_length=300, unique=True)
    short_name = models.CharField(max_length=15, unique=True)
    slug = models.SlugField(unique=True, blank=False)
    icon = models.ImageField(upload_to=image_folder)

    def get_absolute_url(self):
        return reverse('partner_detail_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"

    def __str__(self):
        return self.short_name
