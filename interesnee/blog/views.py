from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from blog.forms import ImpressionForm
from blog.models import Impression


class BaseView(View):
    """Контроллер для главной страницы."""

    def get(self, request, *args, **kwargs):
        """Рендерит главную страницу при GET запросе."""
        form = ImpressionForm
        if request.user.is_authenticated:
            impressions = Impression.objects.filter(owner=request.user)
        else:
            impressions = False
        context = {
            'form': form,
            'maps_api_key': settings.GOOGLE_MAPS_API_KEY,
            'impressions': impressions,
        }
        return render(request, 'base.html', context)


class CreateImpressionView(View):
    """Контроллер для создания нового впечатления."""

    def post(self, request, *args, **kwargs):
        """При получении POST запроса проверяем валидность формы и сохраняем её."""
        form = ImpressionForm(request.POST or None)
        if form.is_valid():
            impression = form.save(commit=False)
            impression.title = form.cleaned_data.get('title')
            impression.text = form.cleaned_data.get('text')
            impression.latitude = form.cleaned_data.get('latitude')
            impression.longitude = form.cleaned_data.get('longitude')
            impression.owner = request.user
            form.save()
        return HttpResponseRedirect(reverse('base'))
