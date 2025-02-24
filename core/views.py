from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def billing(request):
    return render(request, "billing/billing.html")