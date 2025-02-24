from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'package', 'status', 'payment_day', 'phone_number', 'accumulated_classes']
    list_filter = ['status', 'package']
    search_fields = ['name', 'phone_number']