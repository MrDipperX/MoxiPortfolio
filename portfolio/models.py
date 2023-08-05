from django.db import models
from django.urls import reverse


class Themes(models.Model):
    name = models.CharField(max_length=250, blank=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    cover = models.ImageField(upload_to="files/%Y/%m/%d", verbose_name='Обложка')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    slug = models.SlugField(max_length=250, db_index=True, unique=True, verbose_name="url")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тему'
        verbose_name_plural = 'Темы'
        ordering = ['time_create', 'name']

    def get_absolute_url(self):
        return reverse('details', kwargs={'theme_slug': self.slug})

    @property
    def get_photos_from_one_theme(self):
        return self.files_set.all()


class Files(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Заголовок')
    description = models.TextField(blank=True, verbose_name='Описание')
    file = models.ImageField(upload_to="files/%Y/%m/%d", verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')
    theme = models.ForeignKey(Themes, on_delete=models.SET_NULL, null=True, verbose_name='Тема')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Работу'
        verbose_name_plural = 'Работы'
        ordering = ['time_create', 'title']



