from django.db import models


class Impression(models.Model):
    """Модель для впечатлений."""

    title = models.CharField(verbose_name='Заголовок', max_length=100)
    text = models.TextField(verbose_name='Контент впечатления')
    latitude = models.DecimalField(verbose_name='Широта', max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(verbose_name='Долгота', max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.title