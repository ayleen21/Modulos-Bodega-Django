from django.http.response import JsonResponse
from django.urls import reverse_lazy
from app.erp.forms import NicheForm, SegmentForm
from app.erp.mixins import ValidatePermissionRequiredMixin
from app.erp.models import Niche, Segment
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# class EnterpriseListView(LoginRequiredMixin, ListView):
#     model = Enterprise
#     template_name = 'enterprise/list.html'
#     success_url = reverse_lazy('enterprise_list')

#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             action = request.POST['action']
#             if action == 'searchdata':
#                 data = []
#                 for i in Enterprise.objects.all():
#                     data.append(i.toJSON())
#             else:
#                 data['error'] = 'Ha ocurrido un error'
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data, safe=False)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Listado de empresas'
#         context['create_url'] = reverse_lazy('erp:enterpriseCreate')
#         return context


# class EnterpriseCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
#     model = Enterprise
#     form_class = EnterpriseForm
#     template_name = 'customer/create.html'
#     success_url = reverse_lazy('erp:enterprise_list')
#     permission_required = 'add_Enterprise'
#     url_redirect = success_url

#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             action = request.POST['action']
#             if action == 'search_niche_id':
#                 data = [{'id': '', 'text': '------------'}]
#                 for i in Niche.objects.filter(segment_id=request.POST['id']):
#                     data.append({'id': i.id, 'text': i.name, 'data': i.segment.toJSON()})

#             elif action == 'add':
#                     form = self.get_form()
#                     data = form.save()

#             elif action == 'autocomplete':
#                 data = []
#                 for i in Segment.objects.filter(name__icontains=request.POST['term'])[0:10]:
#                     item = i.toJSON()
#                     item['text'] = i.name
#                     data.append(item)
#             else:
#                 data['error'] = 'Ha ocurrido un error'
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data, safe=False)
        

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Creación una empresa/cliente'
#         context['entity'] = 'Empresa'
#         context['list_url'] = self.success_url
#         context['action'] = 'add'
#         return context

class SegmentCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Segment
    form_class = SegmentForm
    template_name = 'enterprise/create_segment.html'
    success_url = reverse_lazy('erp:client_list')
    # permission_required = 'add_Enterprise'
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
            # else:
            #     data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un segmento'
        context['entity'] = 'Empresa'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

class NicheCreateView(LoginRequiredMixin, CreateView):
    model = Niche
    form_class = NicheForm
    template_name = 'enterprise/create_niche.html'
    success_url = reverse_lazy('erp:client_list')
    # permission_required = 'add_Enterprise'
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
            # else:
            #     data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un nicho'
        context['entity'] = 'Empresa'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

# class EnterpriseUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
#     model = Enterprise
#     form_class = EnterpriseFormUpdate
#     template_name = 'enterprise/create.html'
#     success_url = reverse_lazy('erp:enterprise_list')
#     permission_required = 'change_client'
#     url_redirect = success_url

#     def dispatch(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return super().dispatch(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             action = request.POST['action']
#             if action == 'edit':
#                 form = self.get_form()
#                 data = form.save()
#             else:
#                 data['error'] = 'No ha ingresado a ninguna opción'
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Edición de una empresa'
#         context['entity'] = 'Empresas'
#         context['list_url'] = self.success_url
#         context['action'] = 'edit'
#         return context


# class EnterpriseDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
#     model = Enterprise
#     template_name = 'enterprise/delete.html'
#     success_url = reverse_lazy('erp:enterprise_list')
#     permission_required = 'deleteClient'
#     url_redirect = success_url

#     def dispatch(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return super().dispatch(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             self.object.delete()
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Eliminación de una empresa'
#         context['entity'] = 'Empresas'
#         context['list_url'] = self.success_url
#         return context