from django.contrib import admin
from Med_ask_test_app.models import Polis, InsuranceCompany, MedicalService


# Register your models here.

class PolisAdmin(admin.ModelAdmin):
    list_display = ("identification_number", "type", "insurance_company", "creation_date", "expiration_date")


class InsuranceCompanyAdmin(admin.ModelAdmin):
    list_display = ("title", "logo", "logo_slug", "phone_number", "creation_date", "insurance_company_medical_services")

    def insurance_company_medical_services(self, obj):
        return "\n".join([str(service.title) + ", " for service in obj.medical_services.all()])


class MedicalServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "creation_date")


admin.site.register(Polis, PolisAdmin)
admin.site.register(InsuranceCompany, InsuranceCompanyAdmin)
admin.site.register(MedicalService, MedicalServiceAdmin)
