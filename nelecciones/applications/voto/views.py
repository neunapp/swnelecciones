# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ipware import get_client_ip
from datetime import datetime, timedelta
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
from applications.home.models import Departamento, Provincia, Distrito
# models
from .models import (
    CandidatoDepartamento,
    CandidatoProvincia,
    CandidatoDistrito,
    ConsejeroDepartamento,
    VotoRegion,
    VotoConsejero,
    VotoProvincia,
    VotoDistrito
)


class ListaCandidatosView(ListView):
    """ vista que lista candidatos"""

    context_object_name = 'candidatos'
    template_name = 'voto/candidatos.html'

    def get_context_data(self, **kwargs):
        context = super(ListaCandidatosView, self).get_context_data(**kwargs)
        pk_distrito = self.kwargs.get('pk', 0)
        flat = self.kwargs.get('flat', 0)
        if flat == 'T':
            context['msj'] = 'Voto Registrado'
        elif flat == 'E':
            context['msj'] = 'No puede duplicar el voto'
        else:
            context['msj'] = ' '
        distrito = Distrito.objects.get(pk=pk_distrito)
        context['region'] = distrito.provincia.departamento.name
        context['provincia'] = distrito.provincia.name
        context['distrito'] = distrito
        return context

    def get_queryset(self):
        #recuperamos el valor por GET
        pk_distrito = self.kwargs.get('pk', 0)
        distrito = Distrito.objects.get(pk=pk_distrito)
        #
        consulta = {
            'regionales': CandidatoDepartamento.objects.filter(departamento__id=distrito.provincia.departamento.pk),
            'consejeros': ConsejeroDepartamento.objects.filter(departamento__id=distrito.provincia.departamento.pk),
            'provincias': CandidatoProvincia.objects.filter(provincia__id=distrito.provincia.pk),
            'distritos': CandidatoDistrito.objects.filter(distrito__id=distrito.pk),
        }
        return consulta


class ListaResultadosView(ListView):
    """ vista que lista resultados de encuesta"""

    context_object_name = 'resultados'
    template_name = 'voto/resultados.html'

    def get_context_data(self, **kwargs):
        context = super(ListaResultadosView, self).get_context_data(**kwargs)
        pk_distrito = self.kwargs.get('pk', 0)
        distrito = Distrito.objects.get(pk=pk_distrito)
        context['region'] = distrito.provincia.departamento.name
        context['provincia'] = distrito.provincia.name
        context['distrito'] = distrito
        return context

    def get_queryset(self):
        #recuperamos el valor por GET
        pk_distrito = self.kwargs.get('pk', 0)
        distrito = Distrito.objects.get(pk=pk_distrito)
        #
        consulta = {
            'regionales': VotoRegion.objects.lista_resultados_7(),
            'consejeros': VotoConsejero.objects.lista_resultados_7(),
            'provincias': VotoProvincia.objects.lista_resultados_7(),
            'distritos': VotoDistrito.objects.lista_resultados_7(),
        }
        return consulta


class VotoView(View):
    """
    Registramos voto
    """
    def get(self, request, *args, **kwargs):
        cod = self.kwargs.get('cod', 0) # codigo para verificar tabla
        pk = self.kwargs.get('pk', 0) # id de objeto enviado
        distrito = self.kwargs.get('distrito', 0) # id de objeto enviado
        client_ip, is_routable = get_client_ip(request) # recuperamos la ip del usuario
        mensaje = 'T'
        if client_ip:
            print('registrando .....')
            if cod == '0':
                # voto departamental
                electo = CandidatoDepartamento.objects.get(id=pk)
                voto = VotoRegion(
                    electo=electo,
                    ippc=client_ip,
                    date=datetime.now().date()
                )
                try:
                    voto.save()
                except:
                    print('error de duplicado...')
                    mensaje = 'E'
            #
            elif cod == '1':
                # voto departamental
                electo = ConsejeroDepartamento.objects.get(id=pk)
                voto = VotoConsejero(
                    electo=electo,
                    ippc=client_ip,
                    date=datetime.now().date()
                )
                try:
                    voto.save()
                except:
                    print('error de duplicado...')
                    mensaje = 'E'

            elif cod == '2':
                # voto departamental
                electo = CandidatoProvincia.objects.get(id=pk)
                voto = VotoProvincia(
                    electo=electo,
                    ippc=client_ip,
                    date=datetime.now().date()
                )
                try:
                    voto.save()
                except:
                    print('error de duplicado...')
                    mensaje = 'E'

            elif cod == '3':
                # voto departamental
                electo = CandidatoDistrito.objects.get(id=pk)
                voto = VotoDistrito(
                    electo=electo,
                    ippc=client_ip,
                    date=datetime.now().date()
                )
                try:
                    voto.save()
                except:
                    print('error de duplicado...')
                    mensaje = 'E'
            else:
                print('opcion errorea.....')
        #
        return HttpResponseRedirect(
            reverse(
                'voto_app:cedula_list',
                kwargs={
                    'pk': distrito,
                    'flat': mensaje
                },
            )
        )
