# enrollment/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('enroll/', views.enrollment_form, name='enrollment_form'),
    path('generate-csv/', views.generate_csv, name='generate_csv'),
    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),
]
