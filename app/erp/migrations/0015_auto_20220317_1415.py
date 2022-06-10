# Generated by Django 3.2.5 on 2022-03-17 14:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0014_sale_headquarters'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='plans',
            field=models.CharField(choices=[('DOBLE EMCALITV PLATA', 'DOBLE EMCALITV PLATA'), ('DOBLE EMCALITV PLUS ORO', 'DOBLE EMCALITV PLUS ORO'), ('DOBLE EMCALITV PLUS DIAMANTE', 'DOBLE EMCALITV PLUS DIAMANTE'), ('TRIPLE EMCALITV PLATA', 'TRIPLE EMCALITV PLATA'), ('TRIPLE EMCALITV ORO', 'TRIPLE EMCALITV ORO'), ('TRIPLE EMCALITV DIAMANTE', 'TRIPLE EMCALITV DIAMANTE')], default=1, max_length=80, verbose_name='Planes Disponibles'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sale',
            name='pool_ip',
            field=models.CharField(blank=True, choices=[('28', '28'), ('29', '29'), ('30', '30')], max_length=10, null=True, verbose_name='Pool ip'),
        ),
        migrations.AddField(
            model_name='sale',
            name='speed',
            field=models.CharField(choices=[('5MB', '5MB'), ('10MB', '10MB'), ('15MB', '15MB'), ('25MB', '25MB'), ('80MB', '80MB'), ('100MB', '100MB'), ('200MB', '200MB'), ('300MB', '300MB')], default=1, max_length=10, verbose_name='Velocidad'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sale',
            name='static_ip',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message='Por favor,ingrese una ip valida', regex='^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')], verbose_name='Ip FIja'),
        ),
    ]
