import os
from django.conf import settings
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from system.decorators import unauthenticated_user
from .models import Accessories
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from django.utils.safestring import mark_safe


# Register your models here.
@unauthenticated_user
def index(request):
    accessories = Accessories.objects.all()
    return render(request, 'main_view/templates/accessories/index.html',{'accessories':accessories})
    
@unauthenticated_user
def add(request):
    return render(request, 'main_view/templates/accessories/add.html')

@unauthenticated_user
def store(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        print(id)
        if id is not None:
            form = request.POST
            accessories = Accessories.objects.get(id = id)
            accessories.name=form['Name']
            accessories.description=form['Description']
            image= request.FILES.get('Image')
            if image is not None:
                accessories.image= image
            accessories.quantity=form['Quantity']
            accessories.price=form['Price']
            accessories.save(user=request.user)
        else:
            form = request.POST
            accessories = Accessories()
            accessories.name = form['Name']
            accessories.description = form['Description']
            accessories.price = form['Price']
            accessories.quantity = form['Quantity']
            accessories.image = request.FILES.get('Image')
            accessories.save(user=request.user)
            print(request.user.id)
    return HttpResponseRedirect('/admin/accessories/')

@unauthenticated_user
def edit(request):
    id = request.GET.get('id')
    accessories = Accessories.objects.get(id=id)
    return render(request, 'main_view/templates/accessories/edit.html',{'accessories':accessories})

def delete(request):
    id = request.GET.get('id')
    print(id)
    accessories = Accessories.objects.get(id=id)
    accessories.deleted_by = request.user.id
    
    old_icon = accessories.image
    old_icon_path = os.path.join(settings.MEDIA_ROOT, str(old_icon))
    if os.path.isfile(old_icon_path):
        os.remove(old_icon_path)
    accessories.image = None
    accessories.save()
    accessories.delete()
    response = {
        'msg': 'Deleted',
        'success': True
    }
    data = mark_safe(json.dumps(response, indent=4, sort_keys=True, default=str))
    return HttpResponseRedirect('/admin/accessories/')