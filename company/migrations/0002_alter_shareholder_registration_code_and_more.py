# Generated by Django 5.1.4 on 2024-12-16 11:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shareholder',
            name='registration_code',
            field=models.CharField(blank=True, max_length=7, null=True, verbose_name='Registrikood'),
        ),
        migrations.AlterField(
            model_name='shareholder',
            name='share_amount',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2500, 'Osa suurus peab olema vähemalt 2500 eurot.')], verbose_name='Osa suurus (EUR)'),
        ),
        migrations.AlterField(
            model_name='shareholder',
            name='shareholder_type',
            field=models.CharField(choices=[('1', 'Füüsiline isik'), ('2', 'Juriidiline isik')], max_length=20, verbose_name='Osaniku tüüp'),
        ),
    ]