from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from django.urls import reverse

from blog.models import Impression
from blog.views import CreateImpressionView


class NotAuthUserBaseViewTest(TestCase):
    """Класс тестов для контроллера BaseView, для не авторизованного пользователя."""

    def test_view_url_exists_at_desired_location(self):
        """Проверяет, что страница доступна по ссылке - '/'."""
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """Проверяет, что страница доступна по названию ссылки - base."""
        response = self.client.get(reverse('base'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Проверяет, что страница отобржается шаблоном - base.html."""
        response = self.client.get(reverse('base'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')


class AuthUserBaseViewTest(TestCase):
    """Класс тестов для контроллера BaseView, для авторизованного пользователя."""

    def setUp(self):
        """Создаёт двух пользоватлей и по пять воспоминаний для каждого из них."""
        test_user1 = User.objects.create_user(username='test_user1', password='12345')
        test_user1.save()
        test_user2 = User.objects.create_user(username='test_user2', password='12345')
        test_user2.save()

        number_of_impressions = 5
        base_latitude = 56.088129
        base_longitude = 92.919617

        for number_of_impression in range(number_of_impressions):
            Impression.objects.create(
                owner=test_user1,
                title=f'Воспоминание №{number_of_impression} у test_user1',
                text=f'Текст №{number_of_impression} у test_user1',
                latitude=base_latitude - number_of_impression,
                longitude=base_longitude - number_of_impression,
            )
            Impression.objects.create(
                owner=test_user2,
                title=f'Воспоминание №{number_of_impression} у test_user2',
                text=f'Текст №{number_of_impression} у test_user2',
                latitude=base_latitude + number_of_impression,
                longitude=base_longitude + number_of_impression,
            )

    def test_view_url_exists_at_desired_location(self):
        """Проверяет, что страница доступна по ссылке - '/'."""
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """Проверяет, что страница доступна по названию ссылки - base."""
        response = self.client.get(reverse('base'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Проверяет, что страница отобржается шаблоном - base.html."""
        response = self.client.get(reverse('base'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_impressions_only_user(self):
        """Проверяет, что у пользователя отображаются только его воспоминания."""
        self.client.login(username='test_user1', password='12345')
        response = self.client.get(reverse('base'))

        self.assertEquals(str(response.context['user']), 'test_user1')
        self.assertEquals(response.status_code, 200)

        self.assertTrue('impressions' in response.context)

        for impression in response.context['impressions']:
            self.assertEquals(response.context['user'], impression.owner)


class CreateImpressionViewTest(TestCase):
    """Класс тестов для контроллера CreateImpressionView."""

    def setUp(self):
        """Создаёт тестового пользователя."""
        self.user = User.objects.create(username='test_user', password='test_pass')

    def test_302_if_not_login_user(self):
        """Проверяет, что возвращается 302 код, если пользователь не авторизован."""
        response = self.client.post(reverse('create_impression'))
        self.assertEquals(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/create-impression/')

    def test_save_form(self):
        """Проверяет, что переданная форма сохраняется в базу данных."""
        factory = RequestFactory()
        request = factory.post('')
        request.user = self.user
        request.POST = {
            'title': 'test_title',
            'text': 'test_text',
            'latitude': 56.088129,
            'longitude': 92.919617,
        }
        CreateImpressionView.as_view()(request)
        self.assertEqual(Impression.objects.count(), 1)

    def test_save_form_with_invalid_data(self):
        """Проверяет, что форма с неверными данными не сохраняется в базу данных."""
        factory = RequestFactory()
        request = factory.post('')
        request.user = self.user
        request.POST = {
            'title': 'test_title',
            'text': 'test_text',
            'latitude': 'wrong data',
            'longitude': 92.919617,
        }
        CreateImpressionView.as_view()(request)
        self.assertEqual(Impression.objects.count(), 0)
