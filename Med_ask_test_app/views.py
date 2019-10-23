from rest_framework import generics
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response


# Запросы делать на Jquery !

class GetPolis(APIView):  # Проверяет по идентификатору, существует ли полис
    def get(self, request):
        try:
            polis = Polis.objects.get(identification_number=request.GET.get("identificator"))
            serializer = PolisSerializer(polis)
            return Response({"has_been_found": True, "data": serializer.data})
        except Polis.DoesNotExist:
            return Response({"has_been_found": False})


class CheckMedicalServices(APIView):  # Проверяет медицинские услуги
    def post(self, request):
        try:
            polis = Polis.objects.get(identification_number=request.data.get("identificator"))
            polis_serializer = PolisSerializer(polis)
        except Polis.DoesNotExist:
            return Response({"polis_has_been_found": False})
        insurance_company = InsuranceCompany.objects.get(title=request.data.get("insurance_company"))
        insurance_type = request.data.get("insurance_type")
        insurance_company_serializer = InsuranceCompanySerializer(insurance_company)

        chosen_medical_services = request.data.getlist('chosen_medical_services[]')

        affordable = []
        unaffordable = []
        nonexistent = []
        for medical_service in chosen_medical_services:
            if MedicalService.objects.filter(title=medical_service):
                if insurance_company.medical_services.filter(title=medical_service):
                    affordable.append(medical_service)
                else:
                    unaffordable.append(medical_service)
            else:
                nonexistent.append(medical_service)
        return Response(
            {"polis": polis_serializer.data, "insurance_company": insurance_company_serializer.data,
             "insurance_type": insurance_type, "affordable": affordable, "unaffordable": unaffordable,
             "nonexistent": nonexistent, "polis_has_been_found": True})


class InsuranceCompaniesList(generics.ListAPIView):  # Получает лист страховых компаний
    queryset = InsuranceCompany.objects.all()
    serializer_class = InsuranceCompanySerializer

    def get(self, request, *args):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response({"data": serializer.data})


class MedicalServicesList(generics.ListAPIView):  # Получает лист медуслуг
    queryset = MedicalService.objects.all()
    serializer_class = MedicalServiceSerializer

    def get(self, request, *args):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response({"data": serializer.data})
