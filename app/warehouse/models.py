from distutils.command.upload import upload
from django.core.validators import RegexValidator
from django.db import models
from django.db import models
from datetime import datetime
from django.forms import  model_to_dict
from gestionservicios.settings import MEDIA_URL, STATIC_URL
from multiselectfield import MultiSelectField

import pkg_resources
from app.models import *
from app.warehouse.choices import devices_choices,brands_choices,products_choices


# REGEXP VALIDATORS ------------------------------------------------------------------------
REGEX_NAME = RegexValidator()


class Device(BaseModelDevice):
    
    
    name = models.CharField(max_length=12, choices=devices_choices, blank=False, verbose_name='Dispositivo')

    brand = models.CharField(max_length=12,choices=brands_choices,verbose_name='Marca')
    
    mac = models.CharField(max_length=12,verbose_name='Mac',
            validators=[
            RegexValidator(
                regex='^[0-9A-F]+$',
                message='La mac digitada es incorrecta'
            )
        ])
    
    model= models.CharField(max_length=12, verbose_name='Modelo',
            validators=[
            RegexValidator(
                regex='^[A-Z0-9\s,\\\/-]*$',
                message='El modelo digitado es incorrecto',
            ),
        ])
    serial = models.CharField(max_length=20,blank=False, verbose_name='Serial',
            validators=[
            RegexValidator(
                regex='^[A-Za-z0-9\s]+[A-Za-z0-9\s]+$(\.0-9+)?',
                message='El serial digitado es incorrecto'
            ),
        ])
    
    value = models.DecimalField(max_digits=9, decimal_places=3,blank=False,verbose_name='Valor',
        validators=[
        RegexValidator(
            regex='[+-]?([0-9]*[.])?[0-9]+',
            message='El valor ingresado es incorrecto'
        )
   ])
    
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripcion')
    
    image = models.ImageField(upload_to='device/%Y/%m/%d', verbose_name='Imagen', blank=True, null=True)
    
    def description_null(self):
        if self.description is None:
            return "Sin descripcion"
        else:
            return self.description
        
    def activation_state(self):
        if self.state == 'E':
            return 'ENTREGADO'
        elif self.state == 'R':
            return 'POR RECOGER'
        elif self.state =='D':
            return 'DISPONIBLE'
        elif self.state == 'B':
            return 'DADO DE BAJA'
        else:
            return ''
        
    def __str__(self):
        return self.name
    
    
    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL,'img/empty.png')
   
        
    def toJSON(self):
        item = model_to_dict(self)
        item['state'] = self.activation_state()
        item['image'] = self.get_image()
        item['description'] = self.description_null()
        return item

    class Meta:
        verbose_name = 'Dispositivo'
        verbose_name_plural = 'Dispositivos'
        ordering = ['id']


class Service(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False,verbose_name='Servicio', 
            validators=[
            RegexValidator(
                regex='^[a-zA-Z]+(\s*[a-zA-Z]*[-.]?)*[a-zA-Z]+$',
                message='El servicio digitado es incorrecto.'
            )
    ])
    
    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        


class subService(models.Model):
    name = models.CharField(max_length=50, verbose_name='Subservicio', null=False, blank=False, 
            validators=[
            RegexValidator(
                regex='^[A-zA-Z0-9\s]*$',
                message='El subservicio digitado es incorrecto.'
            ),
    ])
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Servicio')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Subservicio'
        verbose_name_plural = 'Subservicios'

class Component(models.Model):
    name=models.CharField(default=0,max_length=50,null=True,blank=True,verbose_name='Componente',
            validators=[
            RegexValidator(
                regex='^[a-zA-Z]+(\s*[a-zA-Z]*[-.]?)*[a-zA-Z]+$',
                message='El componente digitado es incorrecto.'
            )
    ])

    sub_service=models.ForeignKey(subService,on_delete=models.CASCADE,verbose_name='Subservicio')
    
    
    def __str__(self):
        return self.name

    
    def toJSON(self):
        item = model_to_dict(self)
        return item
    
    class Meta:
        verbose_name = 'Componente'
        verbose_name_plural = 'Componentes'
        
class Product(BaseModel):
    name = models.CharField(max_length=30,null=False,blank=False,choices=products_choices,verbose_name='Producto')

    
    service = models.ForeignKey(Service,on_delete=models.CASCADE,verbose_name='Servicio')
    
    cod_open = models.CharField(max_length=10,blank=False,verbose_name='Codigo Open',
        validators=[
        RegexValidator(
            regex='^[0-9]*$',
            message='El codigo ingresado es incorrecto'
            ),
        ])
    
    sub_service = models.ForeignKey(subService,on_delete=models.CASCADE,verbose_name='Subservicio')
    
    component = models.ForeignKey(Component,on_delete=models.CASCADE,verbose_name='Componente')
    
    device = MultiSelectField(choices= devices_choices,verbose_name='Dispositivo')

    description = models.CharField(max_length=500,null=True,blank=True,verbose_name='Descripcion')
    
    def description_null(self):
        if self.description is None:
            return "Sin descripcion"
        else:
            return self.description


    def __str__(self):
        return self.name
    
    
    def activation_state(self):
        if self.state is True:
            return '🟢'
        else:
            return '🔴'
        
    def toJSON(self):
        item = model_to_dict(self)
        item['state'] = self.activation_state()
        item['description'] = self.description_null()
        item['service'] = self.service.toJSON()
        item['sub_service'] = self.sub_service.toJSON()
        item['component'] = self.component.toJSON()
        return item

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


