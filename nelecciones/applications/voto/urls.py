# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from . import views

app_name="voto_app"

urlpatterns = [
    #url para pantalla de inicio
    path('cedula-de-sufragio-encuesta/<pk>/xcod<flat>/encuesta-virtual/',
        views.ListaCandidatosView.as_view(),
        name='cedula_list'
    ),
    #url para resultados de encuesta
    path('resultados-de-encuesta-virtual/<pk>/encuesta-peru/3',
        views.ListaResultadosView.as_view(),
        name='resultados_list'
    ),
    path('registrar-voto/<pk>/<cod>/<distrito>/',
        views.VotoView.as_view(),
        name='cedula_add'
    ),
]
