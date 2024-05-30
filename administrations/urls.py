from django.urls import path, include
from . import admin

urlpatterns = [
    # path('', admin.index, name='member_home'),
    # path('accounts/', include('django.contrib.auth.urls')),
    
    path('', admin.index, name='admin_index'),
    path('users/', include('users.urls')),
    path('fish/', include('fish.urls')),
    path('site_settings/', include('site_settings.urls')),
    path('accessories/', include('accessories.urls')),
    
]
