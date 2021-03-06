# Generated by Django 2.2.4 on 2019-10-18 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Med_ask_test_app', '0009_auto_20191017_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurancecompany',
            name='medical_services',
            field=models.ManyToManyField(related_name='insurance_company_medical_services', to='Med_ask_test_app.MedicalService'),
        ),
        migrations.AlterField(
            model_name='polis',
            name='identification_number',
            field=models.CharField(editable=False, max_length=16, unique=True),
        ),
    ]
