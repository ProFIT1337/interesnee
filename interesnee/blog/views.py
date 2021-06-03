from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from blog.forms import ImpressionForm


class BaseView(View):
    """Контроллер для главной страницы."""

    def get(self, request, *args, **kwargs):
        form = ImpressionForm
        context = {'form': form}
        return render(request, 'base.html', context)


class CreateImpressionView(View):
    """Контроллер для создания нового впечатления."""

    def post(self, request, *args, **kwargs):
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

