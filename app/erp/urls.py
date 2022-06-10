
from django.contrib import admin
from django.urls import path
# from app.erp.views.contract.views import ContractCreateView, ContractListView
from app.erp.views.customer.views import ClientDeleteView, ClientListView, ClientCreateView, ClientUpdateView
from app.erp.views.enterprise.views import NicheCreateView, SegmentCreateView
from app.erp.views.headquaters.views import HeadquartersCreateView, HeadquartersDeleteView, HeadquartersListView, HeadquartersUpdateView
from app.erp.views.sale.views import SaleCreateView

# agrupar mi listas
app_name='erp'

urlpatterns = [
    # CLIENT
    path('customer/list/',ClientListView.as_view(),name='client_list'),
    path('customer/add/',ClientCreateView.as_view(),name='clientCreate'),
    path('customer/update/<int:pk>',ClientUpdateView.as_view(),name='clientUpdate'),
    path('customer/delete/<int:pk>',ClientDeleteView.as_view(),name='clientDelete'),

    # HEADQUARTERS
    path('headquarters/list/',HeadquartersListView.as_view(),name='headquarters_list'),
    path('headquarters/add/',HeadquartersCreateView.as_view(),name='headquartersCreate'),
    path('headquarters/update/<int:pk>',HeadquartersUpdateView.as_view(),name='headquartersUpdate'),
    path('headquarters/delete/<int:pk>',HeadquartersDeleteView.as_view(),name='headquartersDelete'),

    path('segment/add/',SegmentCreateView.as_view(),name='segmentCreate'),
    path('niche/add/',NicheCreateView.as_view(),name='nicheCreate'),

    # CONTRACTS
    # path('contract/list/',ContractListView.as_view(),name='contract_list'),
    # path('contract/add/',ContractCreateView.as_view(),name='contractCreate'),


     path('sale/add/',SaleCreateView.as_view(),name='create_sale'),
]
