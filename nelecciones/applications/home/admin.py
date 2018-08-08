from django.contrib import admin

# Register your models here.
from .models import Departamento, Distrito, Provincia

admin.site.register(Departamento)
admin.site.register(Distrito)
admin.site.register(Provincia)
