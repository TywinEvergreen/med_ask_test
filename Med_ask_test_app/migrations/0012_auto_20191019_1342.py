# Generated by Django 2.2.4 on 2019-10-19 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Med_ask_test_app', '0011_remove_polis_medical_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polis',
            name='identification_number',
            field=models.CharField(editable=False, max_length=12, unique=True),
        ),
    ]
