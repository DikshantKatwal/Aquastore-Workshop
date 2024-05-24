from django.shortcuts import render


def index(request):
    return render(request, 'main_view/templates/index.html')
