from django.shortcuts import render
from django.views import View


class BaseView(View):
    """Контроллер для главной страницы."""

    def get(self, request, *args, **kwargs):
        return render(request, 'base.html', {})
