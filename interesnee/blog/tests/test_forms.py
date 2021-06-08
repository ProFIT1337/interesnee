from django.test import TestCase

from blog.forms import ImpressionForm


class ImpressionFormTest(TestCase):
    """Класс тестов для формы ImpressionForm."""

    def test_valid_data(self):
        """Проверяет, что форма проходит валидацию с верными данными."""
        form = ImpressionForm(
            data={
                'title': 'test_title',
                'text': 'test_text',
                'latitude': 56.088129,
                'longitude': 92.919617,
            },
        )
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        """Проверяет, что форма не проходит валидацию с неверными данными."""
        form = ImpressionForm(
            data={
                'title': 'test_title',
                'text': 'test_text',
                'latitude': 'false_data',
                'longitude': 92.919617,
            },
        )
        self.assertFalse(form.is_valid())
