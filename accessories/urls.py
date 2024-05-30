from django.urls import path, include
from . import admin


urlpatterns = [
    path('', admin.index, name='accessories_index'),
    path('add/', admin.add, name='accessories_add'),
    path('add/', admin.add, name='accessories_add'),
    path('store/', admin.store, name='store_accessories'),
    path('edit/', admin.edit, name='accessories_edit'),
    path('delete/', admin.delete, name='accessories_delete'),
]
    
