from email.header import Header
from django.core.validators import RegexValidator
from django.db import models
from django.forms import model_to_dict
from datetime import datetime
from simple_history.models import HistoricalRecords
from app.models import *
from app.warehouse.models import Product,Service,subService,Component
from app.erp.choices import gender_choices, cities, t_nit, via_choices, prefix_choices, grouped_choices,terminal_type,grouped_type,pool_ip,plans,speed
# from gestionservicios.settings import MEDIA_URL, STATIC_URL

# REGEXP VALIDATORS ------------------------------------------------------------------------
REGEX_NAME = RegexValidator()


class Segment(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False,verbose_name='Segmento', 
            validators=[
            RegexValidator(
                regex='^[A-Za-z ]{3,500}$',
                message='Segmento digitado incorrectamente, verifique que no contenga numeros o simbolos',
            ),
            ])

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Segmento'
        verbose_name_plural = 'Segmentos'


class Niche(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nicho', null=False, blank=False, 
            # validators=[
            # RegexValidator(
            #     regex='^[A-Za-z ]{3,500}$',
            #     message='Nicho digitado incorrectamente',
            # ),
            # ]
            )
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE, verbose_name='Segmento')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['name'] = self.name
        item['segment'] = self.segment.toJSON()
        return item

    class Meta:
        verbose_name = 'Nicho'
        verbose_name_plural = 'Nichos'


class Client(BaseModel):

    client_type = models.CharField(max_length=50, null=True, blank=True, verbose_name='Juridico')
    nit_client = models.IntegerField(default = True, blank=False, verbose_name='NIT/DNI',
        validators=[
        RegexValidator(
            regex='^([\d]{1,5})\s?([\d]){5,7}$',
            message='Numero de identificacion digitado incorrectamente verifique que no contenga letras o simbolos',
        ),
    ])
    names = models.CharField(max_length=150, verbose_name='Nombre',         
        validators=[
            RegexValidator(
                regex='^[A-Za-z ]{3,50}$',
                message='Nombre juridico o natural, Verifique que este bien escrito y no contenga simbolos y numeros',
            ),
        ])

    # ADDRESS
    via = models.CharField(max_length=50, choices=via_choices)
    no_via = models.CharField(max_length=50)
    prefix = models.CharField(max_length=50, choices=prefix_choices)
    suffix = models.CharField(max_length=50, choices=prefix_choices)
    generating_via = models.CharField(max_length=50)

    city = models.CharField(max_length=50, choices=cities, blank=False, verbose_name='Ciudad')

    grouped = models.CharField(max_length=50, null=True, blank=True)
    group_type = models.CharField(max_length=50, choices=grouped_type, null=True, blank=True)
    group_number = models.CharField(max_length=50, null=True, blank=True)
    type_terminal = models.CharField(max_length=50, choices=terminal_type, null=True, blank=True)
    number_terminal = models.CharField(max_length=50, null=True, blank=True)


    phone = models.CharField(max_length=15, null=False, blank=False, verbose_name='Telefono', 
            validators=[
            RegexValidator(
                regex='^([\d]{5,5})\s?([\d]){5,5}$',
                message='Numero telefonico digitado incorrectamente, verifique que no tenga letras ni simbolos',
            ),
        ])
    email = models.EmailField(max_length=254, verbose_name="Email")
    
    # ENTERPRISE
    legal_representative = models.CharField(max_length=50, null=True, blank=True, verbose_name='Representante legal',
        validators=[
            RegexValidator(
                regex='^[A-Za-z ]{3,50}$',
                message='Representante legal digitado incorrectamente, verifique que no contega numeros o simbolos',
            ),
        ])
    niche = models.ForeignKey(Niche, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Nicho')
    observations = models.CharField(max_length=500, null=True, blank=True, verbose_name='Observaciones')
    historical = HistoricalRecords()
    # is_actived = models.BooleanField(default = True, null=False, blank=False, verbose_name='Estado')
    
    # def client_type_object(self):
    #     if self.client_type is True:
    #         return '🏭'
    #     else:
    #         return '🧍'
            
            
    
    def none_groups(self):
        if self.group_type is None or self.group_number is None or self.type_terminal is None or self.number_terminal is None:
            return ' '
        else:
            return self.group_type + ' ' + self.group_number + ' ' + self.type_terminal + ' ' + self.number_terminal  


    def list_address_with_grouped(self):
        return self.via + ' ' + self.no_via + ' ' + self.prefix + ' #' + self.generating_via + ' ' +self.suffix + '\n' + self.none_groups()
                    

    def observations_null(self):
        if self.observations is None:
            return "Sin observaciones"
        else:
            return self.observations
            
    def empty_fields(self):
        if self.legal_representative is None:
            return "No aplica"
        else:
            t = '{}'.format(self.legal_representative)
            return t.upper()

    def activation_state(self):
        if self.state is True:
            return '🟢'
        else:
            return '🔴'

    def empty_niche_and_segment(self):
        if self.niche is None:
            return {
                'name' : 'No aplica',
                'segment': {'name':'No aplica'},
                } 
        else:
            return self.niche.toJSON()
            
    def get_name(self):
        t = '{}'.format(self.names)
        return t.upper()
    
    def name_nit(self):
        return '{} / {}'.format(self.nit_client, self.names) 
            

    def __str__(self):
        return  str(self.nit_client) + " - " + self.get_name()
            
            
    def toJSON(self):
        item = model_to_dict(self)
        item['names'] = self.get_name()
        item['state'] = self.activation_state()
        item['observations'] = self.observations_null()
        item['legal_representative'] = self.empty_fields()
        item['niche'] = self.empty_niche_and_segment()
        item['segment'] = self.empty_niche_and_segment()
        item['client_type'] = self.client_type
        item['address'] = self.list_address_with_grouped()
        item['full_name'] = self.name_nit()
        return item

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']



# MODELO SEDES
class Headquarters(BaseModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente')
    h_name = models.CharField(max_length=50, verbose_name='Nombre de la sede')

    # ADDRESS
    via = models.CharField(max_length=50, choices=via_choices)
    no_via = models.CharField(max_length=50)
    prefix = models.CharField(max_length=50, choices=prefix_choices)
    suffix = models.CharField(max_length=50, choices=prefix_choices)
    generating_via = models.CharField(max_length=50)

    city = models.CharField(max_length=50, choices=cities, verbose_name='Ciudad')

    grouped = models.CharField(max_length=50, null=True, blank=True)
    group_type = models.CharField(max_length=50, choices=grouped_type, null=True, blank=True)
    group_number = models.CharField(max_length=50, null=True, blank=True)
    type_terminal = models.CharField(max_length=50, choices=terminal_type, null=True, blank=True)
    number_terminal = models.CharField(max_length=50, null=True, blank=True)

    # CONTACT_INFO
    contact_name = models.CharField(max_length=50, verbose_name='Nombre de contacto')
    contact_phone = models.CharField(max_length=50, verbose_name='Telefono de contacto')
    contact_email = models.CharField(max_length=50, verbose_name='Email de contacto')

    observations = models.CharField(max_length=150, null=True, blank=True, verbose_name='Observaciones')
     

    # def list_address(self):
    #     return self.via + ' ' + self.no_via + self.prefix + '#' + self.generating_via + self.suffix

    def none_groups(self):
        if self.group_type is None or self.group_number is None or self.type_terminal is None or self.number_terminal is None:
            return ' '
        else:
            return self.group_type + ' ' + self.group_number + ' ' + self.type_terminal + ' ' + self.number_terminal  

    def list_address_with_grouped(self):
        return self.via + ' ' + self.no_via + ' ' + self.prefix + ' #' + self.generating_via + ' ' +self.suffix + '\n' + self.none_groups()
                    
    def observations_null(self):
        if self.observations is None:
            return "Sin observaciones"
        else:
            return self.observations

    def get_headquarters(self):
        t = '{}'.format(self.h_name)
        return t.capitalize()

    def get_name(self):
        t = '{}'.format(self.contact_name)
        return t.upper()

    def activation_state(self):
        if self.state is True:
            return '🟢'
        else:
            return '🔴'

    def toJSON(self):
        item = model_to_dict(self)
        item['name'] = self.get_headquarters()
        item['contact_name'] = self.get_name()
        item['observations'] = self.observations_null()
        item['state'] = self.activation_state()
        item['client'] = self.client.toJSON()
        item['client_nit'] = self.client.toJSON()
        item['grouped'] = self.grouped
        item['address'] = self.list_address_with_grouped()
        return item

    class Meta:
        verbose_name = 'Sede'
        verbose_name_plural = 'Sedes'
        ordering = ['id']
        

class Sale(models.Model):
    client= models.ForeignKey(Client,on_delete=models.CASCADE)
    headquarters= models.ForeignKey(Headquarters, on_delete=models.CASCADE, verbose_name='Sedes')
    date_joined = models.DateField(default=datetime.now)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='Producto')
    service = models.ForeignKey(Service,on_delete=models.CASCADE,verbose_name='Servicio')
    subservice = models.ForeignKey(subService,on_delete=models.CASCADE,verbose_name='Subservicio')
    component = models.ForeignKey(Component,on_delete=models.CASCADE,verbose_name='Componente')
    speed = models.CharField(max_length=10,choices=speed,verbose_name='Velocidad', )
     
    static_ip = models.CharField(max_length=15,null=True, blank=True,verbose_name='Ip FIja', 
            validators=[
            RegexValidator(
                regex='^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
                message='Por favor,ingrese una ip valida'
            )
        ])
    pool_ip = models.CharField(max_length=10,null=True, blank=True,choices=pool_ip, verbose_name='Pool ip')
    
    dir_server = models.CharField(max_length=40,verbose_name='Dir Server',
            validators=[
            RegexValidator(
                regex='^[aA-zZ0-9\s,\\\/.-:]*$',
                message='Por favor,ingrese una direccion valida'
            )                      
        ])
    
    plans = models.CharField(max_length=80,choices=plans,verbose_name='Planes Disponibles')
    
    def __str__(self):
        return  str(self.nit_client) + " / " + self.get_name()
    
    def get_name(self):
       return '{} / {}'.format(self.nit_client,self.names)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['client'] = self.get_name()
        item['headquarters'] = self.headquarters()
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['product'] = self.product.toJSON()
        item['service'] = self.service.toJSON()
        item['subservice'] = self.subservice.toJSON()
        item['component'] = self.component.toJSON()
        return item

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id'] 
    



