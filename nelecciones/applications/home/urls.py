# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from . import views

app_name="home_app"

urlpatterns = [
    #url para pantalla de inicio
    url(r'^$',
        views.DepartamentosListView.as_view(),
        name='departamento_list'
    ),
    url(r'^provincia-de-procedencia-para-region/(?P<pk>\d+)/provincias-peru/$',
        views.ProvinciasListView.as_view(),
        name='provincia_list'
    ),
    url(r'^distrito-de-procedencia-para-provincia/(?P<pk>\d+)/distritos-peru/$',
        views.DistritoListView.as_view(),
        name='distritos_list'
    ),
    # urls para resultados
    url(r'^resultados-distrito-de-procedencia-para-provincia/(?P<pk>\d+)/distritos-peru/$',
        views.DistritoRListView.as_view(),
        name='distritos_r_list'
    ),
    url(r'^resultados-provincia-de-procedencia-para-region/(?P<pk>\d+)/provincias-peru/$',
        views.ProvinciasRListView.as_view(),
        name='provincia_r_list'
    ),
    url(r'^resultados-encuesta-departamentos-del-peru/$',
        views.DepartamentosRListView.as_view(),
        name='departamento_r_list'
    ),
]
