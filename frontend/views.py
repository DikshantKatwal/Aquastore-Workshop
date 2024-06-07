from django.shortcuts import render

from accessories.models import Accessories
from fish.models import Fish

# Create your views here.
def index(request):
    fishes = Fish.objects.all()
    accessories = Accessories.objects.all()
    print(fishes)
    return render(request, 'frontend/templates/home.html',{
        'fishes':fishes,
        'accessories':accessories
    })