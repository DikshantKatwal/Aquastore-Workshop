from django.urls import path
from . import admin


urlpatterns = [
    path('', admin.index, name='site_settings_index'),
    path('add/', admin.add, name='site_settings_add'),
]