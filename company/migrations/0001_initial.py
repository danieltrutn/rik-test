# Generated by Django 5.1.4 on 2024-12-14 14:41

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Nimi võib sisaldada ainult tähti, numbreid ja tühikuid.', regex='^[a-zA-Z0-9 ]+$')], verbose_name='Nimi')),
                ('registration_code', models.CharField(max_length=7, unique=True, validators=[django.core.validators.RegexValidator(message='Registrikood peab olema täpselt 7 numbrit.', regex='^\\d{7}$')], verbose_name='Registrikood')),
                ('capital', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2500, 'Kapital peab olema vähemalt 2500 eurot.')], verbose_name='Kapital (EUR)')),
                ('establishment_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Asutamiskuupäev')),
            ],
        ),
        migrations.CreateModel(
            name='Shareholder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shareholder_type', models.CharField(choices=[(1, 'Füüsiline isik'), (2, 'Juriidiline isik')], max_length=20, verbose_name='Osaniku tüüp')),
                ('name', models.CharField(max_length=100, verbose_name='Nimi')),
                ('personal_code', models.CharField(max_length=20, verbose_name='Isikukood')),
                ('registration_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='Registrikood')),
                ('share_amount', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1, 'Osa suurus peab olema vähemalt 1 euro.')], verbose_name='Osa suurus (EUR)')),
                ('is_founder', models.BooleanField(default=False, verbose_name='Asutaja')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shareholders', to='company.company')),
            ],
        ),
    ]