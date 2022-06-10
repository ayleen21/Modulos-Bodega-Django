from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from app.erp.mixins import ValidatePermissionRequiredMixin
from app.erp.models import Client, Niche, Segment
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import *
from app.erp.forms import ClientForm
from django.contrib.auth.mixins import LoginRequiredMixin


# class ClientType(TemplateView):
#     # model = Client
#     template_name = 'client_type.html'
#     # success_url = reverse_lazy('client_list')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Tipo de cliente'
#         context['create_person'] = reverse_lazy('erp:clientCreate')
#         context['create_enterprise'] = reverse_lazy('erp:enterpriseCreate')
#         context['list_url'] = reverse_lazy('erp:client_list')
#         return context



# class ClientListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
class ClientListView(ListView):
    model = Client
    template_name = 'customer/list.html'
    success_url = reverse_lazy('client_list')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Client.objects.all():
                    data.append(i.toJSON())
            elif action == 'search_details_client':
                data = []
                for i in Client.objects.filter(id=request.POST['id']):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de personas'
        context['create_url'] = reverse_lazy('erp:clientCreate')
        context['client_create'] = reverse_lazy('erp:client_type')
        return context


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'customer/create.html'
    success_url = reverse_lazy('erp:client_list')
    #permission_required = 'add_client'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_niche_id':
                data = [{'id': '', 'text': '------------'}]
                for i in Niche.objects.filter(segment_id=request.POST['id']):
                    data.append({'id': i.id, 'text': i.name, 'data': i.segment.toJSON()})

            elif action == 'add':
                   form = self.get_form()
                   data = form.save()

            elif action == 'autocomplete':
                 data = []
                 for i in Segment.objects.filter(name__icontains=request.POST['term'])[0:10]:
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
        context['title'] = 'Creación un Cliente'
        context['entity'] = 'Clientes'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'customer/create.html'
    success_url = reverse_lazy('erp:client_list')
    permission_required = 'change_client'
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
        context['title'] = 'Edición de un Cliente'
        context['entity'] = 'Clientes'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'customer/delete.html'
    success_url = reverse_lazy('erp:client_list')
    permission_required = 'deleteClient'
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
        context['title'] = 'Eliminación de un Cliente'
        context['entity'] = 'Clientes'
        context['list_url'] = self.success_url
        return context

