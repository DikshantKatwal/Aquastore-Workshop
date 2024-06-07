from django.shortcuts import render
from system.decorators import unauthenticated_user
from fish.models import Fish
from accessories.models import Accessories

@unauthenticated_user
def index(request):
    accessories = Accessories.objects.all()
    fishes = Fish.objects.all()
    accessories_count = accessories.count()
    fish_count= fishes.count()
    fish_quantity = 0
    accessories_quantity = 0
    for fish in fishes:
        fish_quantity = fish.quantity + fish_quantity
    
    for accessory in accessories:
        accessories_quantity = accessory.quantity + accessories_quantity
    
    print(fish_quantity)
    return render(request, 'main_view/templates/index.html',{
        'fish_count':fish_count,
        'total_fish':fish_quantity,
        'accessories_count':accessories_count,
        'total_accessories':accessories_quantity,

    })
