from django.contrib import admin

from app.warehouse.models import Service,subService,Component,Product 

# Register your models here.
admin.site.register(Service)
admin.site.register(subService)
admin.site.register(Product)
admin.site.register(Component)

