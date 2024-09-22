# coding=utf-8

from django.db import models
from django.utils.text import slugify

class Book(models.Model):
    name = models.CharField(u'Название', max_length=64)
    author = models.CharField(u'Автор', max_length=64)
    pub_date = models.DateField(u'Дата публикации')
    pub_date_slug = models.SlugField(editable=False, unique=True, blank=True)

    def __str__(self):
        return self.name + " " + self.author


    def save(self, *args, **kwargs):
        # Генерация slug из pub_date перед сохранением
        if not self.pub_date_slug:
            pub_date_str = self.pub_date.strftime('%Y-%m-%d')  # Преобразуем дату в строку
            self.pub_date_slug = slugify(pub_date_str)
        super().save(*args, **kwargs)

    def get_pub_date_slug(self):
        """Функция для автоматической генерации pub_date_slug при загрузке данных"""
        if not self.pub_date_slug:
            pub_date_str = self.pub_date.strftime('%Y-%m-%d')
            self.pub_date_slug = slugify(pub_date_str)
