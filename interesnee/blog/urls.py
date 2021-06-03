from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import BaseView, CreateImpressionView

urlpatterns = [
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('create-impression/', CreateImpressionView.as_view(), name='create_impression'),
    path('', BaseView.as_view(), name='base'),
]

