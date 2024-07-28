# enrollment/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .forms import StudentForm
from .models import Student
import csv
from reportlab.pdfgen import canvas

def enrollment_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Student enrolled successfully!'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = StudentForm()
    return render(request, 'enrollment/enrollment_form.html', {'form': form})

def generate_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email', 'Date of Birth'])
    for student in Student.objects.all():
        writer.writerow([student.first_name, student.last_name, student.email, student.date_of_birth])

    return response

def generate_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="students.pdf"'

    p = canvas.Canvas(response)
    students = Student.objects.all()
    for idx, student in enumerate(students):
        p.drawString(100, 700 - idx * 20, f"{student.first_name} {student.last_name} - {student.email} - {student.date_of_birth}")

    p.showPage()
    p.save()
    return response
