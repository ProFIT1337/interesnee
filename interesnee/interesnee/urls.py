import debug_toolbar
from allauth.socialaccount.providers.facebook import views
from allauth.socialaccount.providers.facebook.provider import FacebookProvider
from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns
from allauth.socialaccount.providers.vk.provider import VKProvider
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

# urls для аутентификации ВК
urlpatterns += default_urlpatterns(VKProvider)

# urls для аутентификации Facebook
urlpatterns += default_urlpatterns(FacebookProvider)
urlpatterns += [
    path(
        'facebook/login/token/',
        views.login_by_token,
        name='facebook_login_by_token',
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
