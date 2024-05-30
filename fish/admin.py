import os
from django.conf import settings
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from system.decorators import unauthenticated_user
from .models import Fish
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from django.utils.safestring import mark_safe
# Register your models here.
@unauthenticated_user
def index(request):
    fishes = Fish.objects.all()
    return render(request, 'main_view/templates/fish/index.html',{'fishes':fishes})
    
@unauthenticated_user
def add(request):
    return render(request, 'main_view/templates/fish/add.html')

@unauthenticated_user
def store(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        print(id)
        if id is not None:
            form = request.POST
            fish = Fish.objects.get(id = id)
            fish.name=form['Name']
            fish.description=form['Description']
            image= request.FILES.get('Image')
            if image is not None:
                fish.image= image
            fish.quantity=form['Quantity']
            fish.price=form['Price']
            fish.location=form['Location']
            fish.save(user=request.user)
        else:
            form = request.POST
            fish = Fish()
            fish.name = form['Name']
            fish.description = form['Description']
            fish.location = form['Location']
            fish.price = form['Price']
            fish.quantity = form['Quantity']
            fish.image = request.FILES.get('Image')
            fish.save(user=request.user)
            print(request.user.id)
    return HttpResponseRedirect('/admin/fish')

@unauthenticated_user
def edit(request):
    id = request.GET.get('id')
    fish = Fish.objects.get(id=id)
    return render(request, 'main_view/templates/fish/edit.html',{'fish':fish})

def delete(request):
    id = request.GET.get('id')
    print(id)
    fish = Fish.objects.get(id=id)
    fish.deleted_by = request.user.id
    fish.save()
    fish.delete()
    old_icon = fish.image
    old_icon_path = os.path.join(settings.MEDIA_ROOT, str(old_icon))
    if os.path.isfile(old_icon_path):
        os.remove(old_icon_path)
    fish.delete()
    response = {
        'msg': 'Deleted',
        'success': True
    }
    data = mark_safe(json.dumps(response, indent=4, sort_keys=True, default=str))
    return HttpResponseRedirect('/admin/fish')