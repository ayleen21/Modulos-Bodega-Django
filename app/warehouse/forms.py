from app.warehouse.models import Component, Device,Product, Service, subService
from app.erp.models import Client

from datetime import datetime

from django import forms
from django.forms import ModelForm


class DeviceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Device
        fields = '__all__'
        widgets = {

            'state':forms.Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'

                }
            ),
            
            'name': forms.Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),

            'brand': forms.Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
             'mac': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese la mac del dispositivo'
                }
            ),
            'model': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el modelo del dispositivo'
                }
            ),
            'serial': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el serial del dispositivo'

                }
            ),
            
            'value': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el valor del dispositvo'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'palceholder': 'Ingrese la descripcion del dispositivo',
                    'rows': 3,
                    'cols': 3
                 }
            )
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
    
class ServiceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese un Servicio',
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


class subServiceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = subService
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese un Subservicio',
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
    
class ComponentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Component
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese un Componente',
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
    
class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {

            'state':forms.Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
            
            'name': forms.Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),

            'service': forms.Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
             'cod_open': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el codigo open del servicio'
                }
            ),
            'sub_service': forms.Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'    
                    }
            ),
            'component': forms.Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'  
                }
            ),
            'device': forms.SelectMultiple(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%',

                }
            ),
            'description': forms.Textarea(
                attrs={
                    'palceholder': 'Ingrese la descripcion del producto',
                    'rows': 3,
                    'cols': 3
                 }
            )
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
    
class ProductFormUpdate(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {

            'state':forms.Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
            
            'name': forms.Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),

            'service': forms.Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%',
                    'readonly':'on'
                }
            ),
             'cod_open': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el codigo open del servicio'
                }
            ),
            'sub_service': forms.Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%',
                    'readonly':'on'
                    }
            ),
            'component': forms.Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%',
                    'readonly':'on'
                }
            ),
            'device': forms.SelectMultiple(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%',
 
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'palceholder': 'Ingrese la descripcion del producto',
                    'rows': 3,
                    'cols': 3
                 }
            )
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

