"""gestionservicios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.warehouse.views.device.views import DeviceListView,DeviceCreateView,DeviceUpdateView,DeviceDeleteView
from app.warehouse.views.product.views import ProductDeleteView, ProductListView, ProductCreateView, ProductUpdateView,ServiceCreateView,subServiceCreateView,ComponentCreateView

#agrupar mi listas
app_name='warehouse'

urlpatterns = [
    #device
    path('device/list/',DeviceListView.as_view(),name='device_list'),
    path('device/add/',DeviceCreateView.as_view(),name='deviceCreate'),
    path('device/update/<int:pk>',DeviceUpdateView.as_view(),name='deviceUpdate'),
    path('device/delete/<int:pk>',DeviceDeleteView.as_view(),name='deviceDelete'),
    
    #product
    
    path('product/list/',ProductListView.as_view(),name='product_list'),
    path('product/add/',ProductCreateView.as_view(),name='productCreate'),
    path('product/update/<int:pk>',ProductUpdateView.as_view(),name='productUpdate'),
    path('product/delete/<int:pk>',ProductDeleteView.as_view(),name='productDelete'),


    path('service/add/',ServiceCreateView.as_view(),name='serviceCreate'),
    path('subservice/add/',subServiceCreateView.as_view(),name='subserviceCreate'),
    path('component/add/',ComponentCreateView.as_view(),name='componentCreate'),

    #sale
    

]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)