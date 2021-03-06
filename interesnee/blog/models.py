from django.contrib.auth.models import User
from django.db import models


class Impression(models.Model):
    """Модель для впечатлений."""

    owner = models.ForeignKey(User, verbose_name='Владелец впечатления', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    text = models.TextField(verbose_name='Контент воспоминания')
    latitude = models.DecimalField(verbose_name='Широта', max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(verbose_name='Долгота', max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        """Возвращает строковое представление с названием воспоминания."""
        return self.title
