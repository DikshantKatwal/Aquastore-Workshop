from django.urls import path, include
from . import views


urlpatterns = [
   path('', views.index, name='frontend_index'),
]