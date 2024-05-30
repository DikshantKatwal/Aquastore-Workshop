from django.shortcuts import render
from system.decorators import unauthenticated_user
# Register your models here.

@unauthenticated_user
def index(request):
    return render (request, 'main_view/templates/site_settings/index.html')


def add(request):
    if request.method =='POST':
        print(request.POST)
        companyname= request.POST.get('Name')
        mobile= request.POST.get('Mobile')
        Email= request.POST.get('Email')
        facebook_url= request.POST.get('Facebook')
        instagram_url= request.POST.get('Instagram')
        country= request.POST.get('Country')
        city= request.POST.get('City')
        street= request.POST.get('Street')
        companyname_id = request.user.id
        print(companyname_id)
        return index(request)
    else:
        return index(request)