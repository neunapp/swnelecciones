# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#django library
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    ListView,
    TemplateView,
    View,
)
#local app
from .models import Departamento, Provincia, Distrito


class DepartamentosListView(ListView):
    """ vista que lista departamentos"""

    context_object_name = 'depatamentos'
    template_name = 'home/index.html'

    def get_queryset(self):
        #recuperamos el valor por GET
        return Departamento.objects.all()


class ProvinciasListView(ListView):
    """ vista que lista Provincia"""

    context_object_name = 'provincias'
    template_name = 'home/provincias.html'

    def get_queryset(self):
        #recuperamos el valor por GET
        # pk_departamento = self.kwargs.get('pk', 0)
        pk_departamento = 8
        return Provincia.objects.filter(
            departamento__id=pk_departamento
        )


class DistritoListView(ListView):
    """ vista que lista Provincia"""

    context_object_name = 'distritos'
    template_name = 'home/distritos.html'

    def get_queryset(self):
        #recuperamos el valor por GET
        pk_pro = self.kwargs.get('pk', 0)
        return Distrito.objects.filter(
            provincia__id=pk_pro
        )


class DepartamentosRListView(ListView):
    """ vista que lista departamentos"""

    context_object_name = 'depatamentos'
    template_name = 'voto/departamentos.html'

    def get_queryset(self):
        #recuperamos el valor por GET
        return Departamento.objects.all()


class ProvinciasRListView(ListView):
    """ vista que lista Provincia"""

    context_object_name = 'provincias'
    template_name = 'voto/provincias.html'

    def get_queryset(self):
        #recuperamos el valor por GET
        # pk_departamento = self.kwargs.get('pk', 0)
        return Provincia.objects.filter(
            departamento__id=8
        )


class DistritoRListView(ListView):
    """ vista que lista Provincia"""

    context_object_name = 'distritos'
    template_name = 'voto/distritos.html'

    def get_queryset(self):
        #recuperamos el valor por GET
        pk_pro = self.kwargs.get('pk', 0)
        return Distrito.objects.filter(
            provincia__id=pk_pro
        )

class ContactoTemplateView(TemplateView):
    template_name = 'home/contacto.html'
