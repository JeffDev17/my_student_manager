from django.shortcuts import render
from students.forms import StudentForm

def home(request):
    return render(request, "home.html")

def billing(request):
    return render(request, "billing/billing.html")

def students(request):
    return render(request, "students/students.html")