from app.erp.models import Client, Headquarters, Niche, Segment,Sale

from datetime import datetime

from django import forms
from django.forms import ModelForm


# CLIENTES

class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['names'].widget.attrs['autofocus'] = True

    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'state': forms.Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
            'client_type': forms.CheckboxInput(
                attrs={
                    'style': 'width: 3%;',
                    'id': 'client_type',
                }
            ),
            'names': forms.TextInput(
                attrs={
                    'placeholder': 'Natural o juridico',
                }
            ),

            'nit_client': forms.NumberInput(
                attrs={
                    'placeholder': 'Ingrese documento o NIT',
                }
            ),


            # ADDRESS_FORM
            'via': forms.Select(
                attrs={
                    # 'class': 'select2',
                    'style': 'width: 90%',
                }
            ),
            'no_via': forms.NumberInput(
                attrs={
                    'placeholder': 'Numero de via',
                    'style': 'width: 95%',
                }
            ),
            'prefix': forms.Select(
                attrs={
                    # 'class': 'select2',
                    'style': 'width: 90%',
                }
            ),
            'suffix': forms.Select(
                attrs={
                    # 'class': 'select2',
                    'style': 'width: 90%',
                }
            ),
            'generating_via': forms.TextInput(
                attrs={
                    'placeholder': 'Numero via generadora',
                    'style': 'width: 95%',
                }
            ),
            'city': forms.Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%',
                }
            ),

            
            'grouped': forms.CheckboxInput(
                attrs={
                    'id': 'is_groupedcheckbox',
                    'style': 'width: 100%',
                }
            ),
            'group_type': forms.Select(
                attrs={
                    # 'class': 'select2',
                    'style': 'width: 90%',
                }
            ),
            'group_number': forms.NumberInput(
                attrs={
                    'placeholder': 'Numero de agrupacion',
                    'style': 'width: 95%',
                }
            ),
            'type_terminal': forms.Select(
                attrs={
                    # 'class': 'select2',
                    'style': 'width: 90%',
                }
            ),
            'number_terminal': forms.TextInput(
                attrs={
                    'placeholder': 'Numero de terminal',
                    'style': 'width: 95%',
                }
            ),
            # ADDRESS_FORM


            'legal_representative': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre del representante legal',
                    'id' : 'legal_representative'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Correo electronico',
                }
            ),
            'phone': forms.NumberInput(
                attrs={
                    'placeholder': 'Ingrese telefono de contacto',
                }
            ),   
            'niche': forms.Select(
                attrs={
                    'id': 'niche',
                    'class': 'select2',
                }
            ), 
            'observations': forms.Textarea(
                    attrs={
                        'placeholder': 'Ingrese sus observaciones',
                        'rows': 3,
                        'cols': 3
                    }
                ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                data = instance.toJSON()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


# SEGMENTOS Y NICHOS

class SegmentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Segment
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese un segmento',
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                data = instance.toJSON()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class NicheForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Niche
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese un nicho',
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                data = instance.toJSON()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


# SEDES

class HeadquartersForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['h_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Headquarters
        fields = '__all__'
        widgets = {
            'client': forms.Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),

            'h_name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre de la sede',
                }
            ),

            # ADDRESS_FORM
            'via': forms.Select(
                attrs={
                    # 'class': 'select2',
                    'style': 'width: 90%',
                }
            ),
            'no_via': forms.NumberInput(
                attrs={
                    'placeholder': 'Numero de via',
                    'style': 'width: 95%',
                }
            ),
            'prefix': forms.Select(
                attrs={
                    # 'class': 'select2',
                    'style': 'width: 90%',
                }
            ),
            'suffix': forms.Select(
                attrs={
                    # 'class': 'select2',
                    'style': 'width: 90%',
                }
            ),
            'generating_via': forms.TextInput(
                attrs={
                    'placeholder': 'Numero via generadora',
                    'style': 'width: 95%',
                }
            ),
            'city': forms.Select(
                attrs={
                    # 'class': 'select2',
                    'style': 'width: 100%',
                }
            ),

            
            'grouped': forms.CheckboxInput(
                attrs={
                    'id': 'is_groupedcheckbox',
                    'style': 'width: 100%',
                }
            ),
            'group_type': forms.Select(
                attrs={
                    # 'class': 'select2',
                    'style': 'width: 90%',
                }
            ),
            'group_number': forms.NumberInput(
                attrs={
                    'placeholder': 'Numero de agrupacion',
                    'style': 'width: 95%',
                }
            ),
            'type_terminal': forms.Select(
                attrs={
                    # 'class': 'select2',
                    'style': 'width: 90%',
                }
            ),
            'number_terminal': forms.TextInput(
                attrs={
                    'placeholder': 'Numero de terminal',
                    'style': 'width: 95%',
                }
            ),
            # ADDRESS_FORM
            

            'contact_name': forms.TextInput(
                attrs={
                    # 'class': 'select2',
                    'style': 'width: 100%',
                    'placeholder': 'Digite persona de contacto',
                }
            ),
            'contact_phone': forms.NumberInput(
                attrs={
                    # 'class': 'select2',
                    'style': 'width: 100%',
                    'placeholder': 'Digite telefono de contacto',
                }
            ),
            'contact_email': forms.EmailInput(
                attrs={
                    # 'class': 'select2',
                    'style': 'width: 100%',
                    'placeholder': 'Digite email de contacto',
                }
            ),
            'observations': forms.Textarea(
                attrs={
                    'placeholder': 'Ingrese sus observaciones',
                    'rows': 3,
                    'cols': 3
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                data = instance.toJSON()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class SaleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client'].queryset = Client.objects.none()

    class Meta:
        model = Sale
        fields = '__all__'
        widgets = {
            'client': forms.Select(attrs={
                'class': 'custom-select select2',
                'style': 'width: 80%',
                
                
            }),
             'headquarters': forms.Select(
                attrs={
                'class': 'custom-select select2',
                'style': 'width: 87%',
                
            }),
            
            'date_joined': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker-input',
                    'id': 'date_joined',
                    'data-target': '#date_joined',
                    'data-toggle': 'datetimepicker',
                    'readonly':True,
                    'style': 'width: 100%'

                }
            ),
    
            'service':forms.SelectMultiple(
                attrs={
                    'class': 'select2',
                    
            }),
            'subservice': forms.SelectMultiple(
                attrs={
                    'class': 'select2',
            }),
             'component': forms.SelectMultiple(
                attrs={
                    'class': 'select2',
                    
            }),
            'speed': forms.Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 80%'

                    
            }),
            'static_ip': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese una Ip valida',
                    'style': 'width: 88.8%', 
                   

            }),
            'pool_ip': forms.Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 80%'

                    


            }),
            'plans': forms.Select(
                attrs={
                    'class': 'select2',
            }),
            'dir_server': forms.TextInput(
                attrs={
                    'placeholder': 'Ejemplo:https//192.255.2/emcali/streamming',
                    'style': 'width: 88.8%', 

                   
                   

            }),
        }