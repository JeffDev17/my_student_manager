# core/views.py ou o arquivo de views do seu app
from django.shortcuts import render

def index(request):
    return render(request, 'base.html')  