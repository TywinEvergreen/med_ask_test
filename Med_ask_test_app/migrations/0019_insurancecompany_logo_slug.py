# Generated by Django 2.2.4 on 2019-10-19 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Med_ask_test_app', '0018_auto_20191019_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurancecompany',
            name='logo_slug',
            field=models.SlugField(blank=True),
        ),
    ]