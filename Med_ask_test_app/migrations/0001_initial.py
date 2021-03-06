# Generated by Django 2.2.4 on 2019-10-16 19:01

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('logo', models.ImageField(upload_to='icons/%Y/%m/%d/')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Polis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('MANDATORY', 'ОМС'), ('VOLUNTARY', 'ДМС')], max_length=12)),
                ('identification_number', models.CharField(default=uuid.UUID('d4727e62-b5f4-4e2f-a77e-9e731c17d70e'), editable=False, max_length=16)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('expiration_date', models.DateTimeField(editable=False)),
                ('insurance_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Med_ask_test_app.InsuranceCompany')),
                ('medical_services', models.ManyToManyField(related_name='polis_medical_services', to='Med_ask_test_app.MedicalService')),
            ],
        ),
    ]
