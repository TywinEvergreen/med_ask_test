# Generated by Django 2.2.4 on 2019-10-17 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Med_ask_test_app', '0008_auto_20191017_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polis',
            name='identification_number',
            field=models.CharField(default='3195727504428761', editable=False, max_length=16, unique=True),
        ),
    ]