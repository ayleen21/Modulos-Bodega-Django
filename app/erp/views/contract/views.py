import json
import os

from django.db.models import Q
from app.erp.forms import ClientForm, ContractForm
from app.erp.models import Client, Contract, DetContract, Product, Service
from django.db import transaction
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, View

class ContractListView(ListView):
    model = Contract
    template_name = 'contract/list.html'
    # permission_required = 'view_contract'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Contract.objects.all()[0:15]:
                    data.append(i.toJSON())
            elif action == 'search_details_prod':
                data = []
                for i in DetContract.objects.filter(contract_id=request.POST['id']):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Contratos'
        context['create_url'] = reverse_lazy('erp:contractCreate')
        context['list_url'] = reverse_lazy('erp:contract_list')
        context['entity'] = 'Contratos'
        return context


class ContractCreateView(CreateView):
    model = Contract
    form_class = ContractForm
    template_name = 'contract/create.html'
    success_url = reverse_lazy('erp:contract_list')
    # permission_required = 'add_sale'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_products':
                data = []
                prods = Service.objects.filter(name__icontains=request.POST['term'])[0:10]
                for i in prods:
                    item = i.toJSON()
                    item['value'] = i.name
                    data.append(item)
            elif action == 'add':
                with transaction.atomic():
                    vents = json.loads(request.POST['vents'])
                    sale = Contract()
                    sale.date_joined = vents['date_joined']
                    sale.contract_cli_id = vents['contract_cli']
                    # sale.contract_enterprise_id = vents['contract_enterprise']
                    sale.subtotal = float(vents['subtotal'])
                    sale.total = float(vents['total'])
                    sale.save()

                    for i in vents['products']:
                        det = DetContract()
                        det.contract_id = sale.id
                        det.prod_id = i['id']
                        det.cant = int(i['cant'])
                        det.price = float(i['pvp'])
                        det.subtotal = float(i['subtotal'])
                        det.save()
                        # det.prod.stock -= det.cant
                        det.prod.save()
                    data = {'id': sale.id}
                
            else:
                data['error'] = 'No ha ingresado ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Contrato'
        context['entity'] = 'Contratos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['det'] = []
        context['frmClient'] = ClientForm()
        return context