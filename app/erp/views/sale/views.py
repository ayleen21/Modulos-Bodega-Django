
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.urls import *

from app.erp.forms import ClientForm, SaleForm
from django.views.generic import CreateView

import json
import os
from django.conf import settings
from django.db.models import Q
from app.erp.models import Headquarters, Sale,Client


class SaleCreateView(CreateView):
    model = Sale
    form_class = SaleForm
    template_name = 'sale/create_sale.html'
    success_url = reverse_lazy('erp:create_sale')
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_clients':
                data = []
                term = request.POST['term'].strip()
                clients = Client.objects.filter(Q(names__icontains=term) | Q(nit_client__icontains=term))[0:10]
                for i in clients:
                    item = i.toJSON()
                    item['text'] = i.name_nit()
                    data.append(item)
            elif action == 'create_client':
                frmClient = ClientForm(request.POST)
                data =frmClient.save()
            elif action:
                action = request.POST['action']
                if action == 'search_headquarters':
                    data = []
                    term = request.POST['term'].strip()
                    headquarters = Headquarters.objects.filter(h_name__icontains=request.POST['term'])[0:10]
                for i in headquarters:
                    item = i.toJSON()
                    item['text'] = i.get_name_headquarters()
                    data.append(item)
           
            else:
                data['error'] = 'No ha ingresado ninguna opcion' 
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data,safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creacion de una venta'
        context['entity'] = 'Ventas'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['frmClient'] = ClientForm()
        return context
