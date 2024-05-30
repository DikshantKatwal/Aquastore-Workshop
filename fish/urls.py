from django.urls import path, include
from . import admin


urlpatterns = [
    path('', admin.index, name='fish_index'),
    path('add/', admin.add, name='fish_add'),
    path('store/', admin.store, name='store_fish'),
    path('edit/', admin.edit, name='fish_edit'),
    path('delete/', admin.delete, name='fish_delete'),
]