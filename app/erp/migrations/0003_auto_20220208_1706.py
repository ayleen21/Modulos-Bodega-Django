# Generated by Django 3.2.5 on 2022-02-08 17:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_alter_client_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='t_nit',
            field=models.CharField(choices=[('Cedula de ciudadania', 'Cedula de ciudadania'), ('Tarjeta de identidad', 'Tarjeta de identidad'), ('Registro Civil', 'Registro Civil'), ('Pasaporte', 'Pasaporte')], default=2, max_length=50, verbose_name='Tipo de documento'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(choices=[('Cali', 'Cali'), ('Palmira', 'Palmira'), ('Yumbo', 'Yumbo'), ('Candelaria', 'Candelaria')], max_length=50, verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='client',
            name='gender',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=10, verbose_name='Genero'),
        ),
        migrations.AlterField(
            model_name='client',
            name='names',
            field=models.CharField(max_length=150, validators=[django.core.validators.RegexValidator(message='Nombre digitado incorrectamente', regex='^[A-Za-z ]{3,50}$')], verbose_name='Nombres'),
        ),
        migrations.AlterField(
            model_name='client',
            name='nit',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='Numero de identificacion digitado incorrectamente', regex='^([\\d]{1,5})\\s?([\\d]){5,7}$')], verbose_name='Documento'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message='Numero digitado incorrectamente', regex='^([\\d]{5,5})\\s?([\\d]){5,5}$')], verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='client',
            name='surnames',
            field=models.CharField(max_length=150, validators=[django.core.validators.RegexValidator(message='Apellido digitado incorrectamente', regex='^[A-Za-z ]{3,50}$')], verbose_name='Apellidos'),
        ),
    ]
