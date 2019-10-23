from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User
from Med_ask_test.settings import BACKEND_URL
import datetime


def create_unique_identificator(model):  # Импортируется в models.py, создает уникальный номер полиса
    while True:
        random_value = User.objects.make_random_password(length=12, allowed_chars='1234567890')
        if not model.objects.filter(identification_number=random_value):
            return random_value


class Polis(models.Model):
    polis_types = (
        ("MANDATORY", "ОМС"),
        ("VOLUNTARY", "ДМС")
    )
    identification_number = models.CharField(unique=True, max_length=12, editable=False)  # Номер страхового полиса
    type = models.CharField(choices=polis_types, max_length=12)  # Тип страхового полиса (ОМС или ДМС)
    insurance_company = models.ForeignKey('InsuranceCompany', on_delete=models.CASCADE)  # Страховая компания
    creation_date = models.DateTimeField(auto_now_add=True)  # Дата создания
    expiration_date = models.DateTimeField(editable=False)  # Дата истекания

    def save(self, *args, **kwargs):
        if not self.pk:  # Этот код выполняется только при создании объекта
            self.identification_number = create_unique_identificator(Polis)  # Создает идентификационный номер полиса
            self.expiration_date = datetime.datetime.now() + relativedelta(years=3)  # Устанавливает срок истекания
        super().save(*args, **kwargs)

    def __str__(self):
        return self.identification_number


class InsuranceCompany(models.Model):
    title = models.CharField(max_length=32, unique=True)  # Название страховой компании
    logo = models.ImageField(upload_to="icons/%Y/%m/%d/")  # Логотип компании
    logo_slug = models.SlugField(editable=False, blank=True, max_length=255)  # Ссылка на лого. Будет создана в save()
    phone_number = PhoneNumberField()  # Телефонный номер
    medical_services = models.ManyToManyField('MedicalService', related_name='insurance_company_medical_services') # Медуслуги, предоставляемые страховой компанией
    creation_date = models.DateTimeField(auto_now_add=True)  # Дата создания

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Стоит в начале, для того, чтобы сохранить logo перед созданием logo_slug
        self.logo_slug = BACKEND_URL + 'media/' + str(self.logo)  # Позволит выводить лого по src
        super().save(*args, **kwargs)  # Сохраняет объект уже вместе с logo_slug

    def __str__(self):
        return self.title


class MedicalService(models.Model):
    title = models.CharField(max_length=128, unique=True)  # Название медуслуги
    creation_date = models.DateTimeField(auto_now_add=True)  # Дата создания

    def __str__(self):
        return self.title
