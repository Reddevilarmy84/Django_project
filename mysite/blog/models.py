from datetime import timezone

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Artiсles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/blog/{self.id}'

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"