from rest_framework import serializers
from .models import *


class MedicalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalService
        fields = ("title", "creation_date")


class InsuranceCompanySerializer(serializers.ModelSerializer):
    medical_services = MedicalServiceSerializer(many=True)

    class Meta:
        model = InsuranceCompany
        fields = ("title", "logo_slug", "phone_number", "creation_date", "medical_services")


class PolisSerializer(serializers.ModelSerializer):
    insurance_company = InsuranceCompanySerializer()

    class Meta:
        model = Polis
        fields = ("identification_number", "type", "insurance_company", "creation_date", "expiration_date")
