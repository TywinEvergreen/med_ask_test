# Generated by Django 2.2.4 on 2019-10-19 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Med_ask_test_app', '0020_auto_20191019_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurancecompany',
            name='logo_slug',
            field=models.SlugField(blank=True, editable=False, max_length=255),
        ),
    ]