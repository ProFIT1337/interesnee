from django.contrib.auth.models import User
from django.db import models
from django.test import TestCase

from blog.models import Impression


class ImpressionModelTest(TestCase):
    """Класс тестов для моделеи Impression."""

    @classmethod
    def setUpTestData(cls):
        """Устанавливает начальные данные для базы."""
        test_user = User.objects.create(username='test_user')
        test_latitude = 56.088129
        test_longitude = 92.919617
        Impression.objects.create(
            owner=test_user,
            title='Some title',
            text='Some text',
            latitude=test_latitude,
            longitude=test_longitude,
        )

    def test_str(self):
        """Проверяет, что строковое представление - название вооспоминания."""
        impression = Impression.objects.get(pk=1)
        self.assertEquals(str(impression), impression.title)

    def test_owner_label(self):
        """Проверяет, что verbose_name поля owner - 'Владелец впечатления'."""
        impression = Impression.objects.get(pk=1)
        field_label = impression._meta.get_field('owner').verbose_name
        self.assertEquals(field_label, 'Владелец впечатления')

    def test_owner_on_delete(self):
        """Проверяет, что метод on_delete - models.Cascade."""
        impression = Impression.objects.get(pk=1)
        field_method = impression._meta.get_field('owner').remote_field.on_delete
        self.assertEquals(field_method, models.CASCADE)

    def test_owner_related_model(self):
        """Проверяет, что owner ссылается на модель User."""
        impression = Impression.objects.get(pk=1)
        related_model = impression.owner.__class__
        self.assertEquals(related_model, User)

    def test_title_label(self):
        """Проверяет, что verbose_name поля title - 'Заголовок'."""
        impression = Impression.objects.get(pk=1)
        field_label = impression._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Заголовок')

    def test_title_max_length(self):
        """Проверяет, что максимальная длинна заголовка - 100 символов."""
        impression = Impression.objects.get(pk=1)
        max_length = impression._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_text_label(self):
        """Проверяет, что verbose_name поля text - 'Контент воспоминания'."""
        impression = Impression.objects.get(pk=1)
        field_label = impression._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'Контент воспоминания')

    def test_latitude_label(self):
        """Проверяет, что verbose_name поля latitude - 'Широта'."""
        impression = Impression.objects.get(pk=1)
        field_label = impression._meta.get_field('latitude').verbose_name
        self.assertEquals(field_label, 'Широта')

    def test_latitude_max_digits(self):
        """Проверяет, что max_digits поля latitude - 9."""
        impression = Impression.objects.get(pk=1)
        received_max_digits = impression._meta.get_field('latitude').max_digits
        self.assertEquals(received_max_digits, 9)

    def test_latitude_null(self):
        """Проверяет, что атрибут null поля latitude - True."""
        impression = Impression.objects.get(pk=1)
        received_value = impression._meta.get_field('latitude').null
        self.assertTrue(received_value)

    def test_latitude_blank(self):
        """Проверяет, что атрибут blank поля latitude - True."""
        impression = Impression.objects.get(pk=1)
        received_value = impression._meta.get_field('latitude').blank
        self.assertTrue(received_value)

    def test_longitude_label(self):
        """Проверяет, что verbose_name поля longitude - 'Долгота'."""
        impression = Impression.objects.get(pk=1)
        field_label = impression._meta.get_field('longitude').verbose_name
        self.assertEquals(field_label, 'Долгота')

    def test_longitude_max_digits(self):
        """Проверяет, что max_digits поля longitude - 9."""
        impression = Impression.objects.get(pk=1)
        received_max_digits = impression._meta.get_field('longitude').max_digits
        self.assertEquals(received_max_digits, 9)

    def test_longitude_null(self):
        """Проверяет, что атрибут null поля longitude - True."""
        impression = Impression.objects.get(pk=1)
        received_value = impression._meta.get_field('longitude').null
        self.assertTrue(received_value)

    def test_longitude_blank(self):
        """Проверяет, что атрибут blank поля longitude - True."""
        impression = Impression.objects.get(pk=1)
        received_value = impression._meta.get_field('longitude').blank
        self.assertTrue(received_value)
