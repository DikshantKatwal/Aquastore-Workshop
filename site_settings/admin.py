from django.shortcuts import render
from system.decorators import unauthenticated_user
from .models import SiteSetting
from django.contrib import messages
from django.http import HttpResponseRedirect
# Register your models here.

@unauthenticated_user
def index(request):
    return render (request, 'main_view/templates/site_settings/index.html')


def add(request):
    SiteSetting.truncate()
    form_data = request.POST
    data_dict = form_data.dict()
    for key, value in data_dict.items():
        site_setting = SiteSetting(key=key, value=value)
        site_setting.save()
    messages.success(request, 'Site setting changed successfully')
    return HttpResponseRedirect('/admin/site_settings')
