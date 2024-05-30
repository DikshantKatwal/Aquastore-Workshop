from django.shortcuts import render
from system.decorators import unauthenticated_user

@unauthenticated_user
def index(request):
    return render(request, 'main_view/templates/index.html')
