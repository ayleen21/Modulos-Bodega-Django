from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from app.warehouse.models import Device
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import *
from app.warehouse.forms import DeviceForm

class DeviceListView(ListView):
    model = Device
    template_name = 'device/list.html'
    success_url = reverse_lazy('device_list')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Device.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de dispositivos'
        context['create_url'] = reverse_lazy('warehouse:deviceCreate')
        return context


class DeviceCreateView(CreateView):
    model = Device
    form_class = DeviceForm
    template_name = 'device/create.html'
    success_url = reverse_lazy('warehouse:device_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Dispositivo'
        context['entity'] = 'Dispositivos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class DeviceUpdateView(UpdateView):
    model = Device
    form_class = DeviceForm
    template_name = 'device/create.html'
    success_url = reverse_lazy('warehouse:device_list')
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
        context['title'] = 'Edición de un Dispositivo'
        context['entity'] = 'Dispositivos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class DeviceDeleteView(DeleteView):
    model = Device
    template_name = 'device/delete.html'
    success_url = reverse_lazy('warehouse:device_list')
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
        context['title'] = 'Eliminación de un Dispositivo'
        context['entity'] = 'Dispositivos'
        context['list_url'] = self.success_url
        return context