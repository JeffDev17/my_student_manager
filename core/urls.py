"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from core import views as core_views
from students import views as student_views

urlpatterns = [
    path('', core_views.home, name='home'),
    path('billing/', core_views.billing, name='billing'),
    path('students/', student_views.students_list, name='students'),
    path('students/new/', student_views.new_student, name='new_student'),
    path('students/delete/<int:pk>/', student_views.delete_student, name='delete_student'),
    path('students/update/<int:pk>/', student_views.update_student, name='update_student'),
]