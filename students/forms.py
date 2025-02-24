from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'start_date', 'package', 'payment_day', 'phone_number', 'status']