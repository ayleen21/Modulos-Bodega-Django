from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse
from app.erp.forms import HeadquartersForm
from app.erp.models import Headquarters
from django.urls import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class HeadquartersListView(LoginRequiredMixin, ListView):
    model = Headquarters
    template_name = 'headquarters/list.html'
    success_url = reverse_lazy('headquarters_list')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Headquarters.objects.all():
                    data.append(i.toJSON())
            elif action == 'search_details_headquarters':
                data = []
                for i in Headquarters.objects.filter(id=request.POST['id']):
                    data.append(i.toJSON())        
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de sedes'
        context['create_url'] = reverse_lazy('erp:headquartersCreate')
        return context


class HeadquartersCreateView(LoginRequiredMixin, CreateView):
    model = Headquarters
    form_class = HeadquartersForm
    template_name = 'headquarters/create.html'
    success_url = reverse_lazy('erp:headquarters_list')
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
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de una sede'
        context['entity'] = 'Sedes'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

class HeadquartersUpdateView(LoginRequiredMixin, UpdateView):
    model = Headquarters
    form_class = HeadquartersForm
    template_name = 'headquarters/create.html'
    success_url = reverse_lazy('erp:headquarters_list')
    permission_required = 'change_headquarters'
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
        context['title'] = 'Edición de una sede'
        context['entity'] = 'Sedes'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class HeadquartersDeleteView(LoginRequiredMixin, DeleteView):
    model = Headquarters
    template_name = 'headquarters/delete.html'
    success_url = reverse_lazy('erp:headquarters_list')
    permission_required = 'deleteHeadquarters'
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
        context['title'] = 'Eliminación de una sede'
        context['entity'] = 'Sedes'
        context['list_url'] = self.success_url
        return context