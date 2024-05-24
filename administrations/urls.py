from django.urls import path, include
from . import admin

urlpatterns = [
    # path('', admin.index, name='member_home'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.index, name='index'),
]
