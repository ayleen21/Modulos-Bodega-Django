from django.contrib import admin

from app.erp.models import Client, Headquarters, Segment,Niche

# Register your models here.
admin.site.register(Client)
admin.site.register(Headquarters)
admin.site.register(Segment)
admin.site.register(Niche)

admin.site.register