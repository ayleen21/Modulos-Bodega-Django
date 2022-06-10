from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from django.urls import reverse_lazy
from app.warehouse.models import Product,Service,subService,Component
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import *
from app.warehouse.forms import ComponentForm, ProductForm, ServiceForm, subServiceForm,ProductFormUpdate

class ServiceCreateView( CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'product/create_service.html'
    success_url = reverse_lazy('warehouse:product_list')
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
         
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un servicio'
        context['entity'] = 'Producto'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

class subServiceCreateView(CreateView):
    model = subService
    form_class = subServiceForm
    template_name = 'product/create_subservice.html'
    success_url = reverse_lazy('warehouse:product_list')
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un subservicio'
        context['entity'] = 'Producto'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context
    
class ComponentCreateView(CreateView):
    model = Component
    form_class = ComponentForm
    template_name = 'product/create_component.html'
    success_url = reverse_lazy('warehouse:product_list')
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un componente'
        context['entity'] = 'Producto'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context
    
class ProductListView(ListView):
    model = Product
    template_name = 'product/list.html'
    success_url = reverse_lazy('product_list')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Product.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Productos'
        context['create_url'] = reverse_lazy('warehouse:productCreate')
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/create.html'
    success_url = reverse_lazy('warehouse:product_list')
    url_redirect = success_url
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_service_id':
                data = [{'id': '', 'text': '------------'}]
                for i in Service.objects.filter(service_id=request.POST['id']):
                    data.append({'id': i.id, 'text': i.name, 'data': i.service.toJSON()})
            
        
            #Action subService
            
            action = request.POST['action']
            if action == 'search_sub_service_id':
                data = [{'id': '', 'text': '------------'}]
                for i in subService.objects.filter(service_id=request.POST['id']):
                    data.append({'id': i.id, 'text': i.name, 'data': i.service.toJSON()})
            
            
            #Action Component
            elif action:
                action = request.POST['action']
                if action == 'search_component_id':
                     data = [{'id': '', 'text': '------------'}]
                for i in Component.objects.filter(sub_service_id=request.POST['id']):
                    data.append({'id': i.id, 'text': i.name, 'data': i.sub_service.toJSON()})
            
            elif action == 'add':
                form = self.get_form()
                data = form.save()
                    
            #Autocomplete Service
            elif action == 'autocomplete':
                data = []
                for i in Service.objects.filter(name__icontains=request.POST['term'])[0:10]:
                    item = i.toJSON()
                    item['text'] = i.name
                    data.append(item)
                    
            #Autocomplete subService
            elif action == 'autocomplete':
                data = []
                for i in subService.objects.filter(name__icontains=request.POST['term'])[0:10]:
                    item = i.toJSON()
                    item['text'] = i.name
                    data.append(item)
                    
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Producto'
        context['entity'] = 'Producto'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductFormUpdate
    template_name = 'product/create.html'
    success_url = reverse_lazy('warehouse:product_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de un Producto'
        context['entity'] = 'Producto'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/delete.html'
    success_url = reverse_lazy('warehouse:product_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Producto'
        context['entity'] = 'Producto'
        context['list_url'] = self.success_url
        return context
