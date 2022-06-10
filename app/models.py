from django.db import models

from django.db import models
from app.warehouse.choices import status_choices

from app.erp.choices import state_choices

class BaseModel(models.Model):

    id = models.AutoField(primary_key=True)
    state = models.BooleanField('Estado', default=True, choices=state_choices)
    created_date = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Fecha de Modificacion', auto_now=True, auto_now_add=False)
    delete_date = models.DateField('Fecha de Eliminacion', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'

class BaseModelDevice(models.Model):

    id = models.AutoField(primary_key=True)
    state = models.CharField('Estado',max_length=15, choices=status_choices)
    created_date = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Fecha de Modificacion', auto_now=True, auto_now_add=False)
    delete_date = models.DateField('Fecha de Eliminacion', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = 'Modelo Base de Dispositivo'
        verbose_name_plural = 'Modelos Base de Dispositivo'