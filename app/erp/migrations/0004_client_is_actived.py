# Generated by Django 3.2.5 on 2022-02-08 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_auto_20220208_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='is_actived',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]
