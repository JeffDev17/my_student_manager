from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from .models import Student

def students_list(request):
    students_list = Student.objects.all()
    return render(request, 'students/students.html', {'students': students_list})

def new_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()
    
    return render(request, 'students/new.html', {'form': form})

def delete_student(request, pk):
    if request.method == "POST":
        student = get_object_or_404(Student, id=pk)
        student.delete()
    return redirect('students')