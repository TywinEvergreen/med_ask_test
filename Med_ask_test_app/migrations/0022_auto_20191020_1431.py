# Generated by Django 2.2.4 on 2019-10-20 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Med_ask_test_app', '0021_auto_20191019_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurancecompany',
            name='title',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
