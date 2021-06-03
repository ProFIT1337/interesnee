from django import forms

from blog.models import Impression


class ImpressionForm(forms.ModelForm):
    """Форма для создания Impression`a."""

    class Meta:
        model = Impression
        fields = ['title', 'text', 'latitude', 'longitude']
