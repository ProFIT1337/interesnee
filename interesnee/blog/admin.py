from django.conf import settings
from django.contrib import admin

from blog.models import Impression


@admin.register(Impression)
class ImpressionAdmin(admin.ModelAdmin):
    """Модель администрирования модели Impression."""

    list_display = ('owner', 'title', 'text', 'latitude', 'longitude')
    search_fields = ('title',)

    fieldsets = (
        (None, {
            'fields': ('owner', 'title', 'text', 'latitude', 'longitude'),
        }),
    )

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('css/admin/location_picker.css',),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                'js/admin/location_picker.js',
            )