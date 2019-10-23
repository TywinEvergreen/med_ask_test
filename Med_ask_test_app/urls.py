from django.urls import path
from .views import *

urlpatterns = [
    path('polis/', GetPolis.as_view()),  # Проверка полиса
    path('insurance_companies/list/', InsuranceCompaniesList.as_view()),  # Список страховых компаний
    path('medical_services/list/', MedicalServicesList.as_view()),  # Список медуслуг
    path('medical_services/check/', CheckMedicalServices.as_view()),  # Список медуслуг
]
