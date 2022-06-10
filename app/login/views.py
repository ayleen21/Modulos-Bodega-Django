from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.views.generic import FormView, RedirectView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import gestionservicios.settings as setting
from gestionservicios import settings
# Create your views here.

class LoginFormView(LoginView):
    template_name = 'login.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context

# class LoginFormView2(FormView):
#     form_class = AuthenticationForm
#     template_name = 'login.html'
#     success_url = reverse_lazy(setting.LOGIN_REDIRECT_URL)

#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return HttpResponseRedirect(self.success_url)
#         return super().dispatch(request, *args, **kwargs)

#     def form_valid(self, form):
#         login(self.request, form.get_user())
#         return HttpResponseRedirect(self.success_url)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Iniciar sesión'
#         return context

class LogoutView(RedirectView):
    pattern_name = 'login:login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)