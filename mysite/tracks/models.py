from django.db import models


# Create your models here.
class Tracks(models.Model):
    title = models.CharField('Название', max_length=100, default='Название трэка')
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Текст песни')
    date = models.DateTimeField('Дата публикации')

# метод __str__ выводит из поля title обьектов бд на страницу
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'
