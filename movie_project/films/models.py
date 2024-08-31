from django.db import models


class films(models.Model):
    title = models.CharField('Название фильма', max_length=50)
    short_description = models.CharField('Краткое описание фильма', max_length=200)
    text = models.TextField('Отзыв')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'