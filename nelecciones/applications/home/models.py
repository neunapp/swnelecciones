# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify
from django.conf import settings
# third-party
from model_utils.models import TimeStampedModel
from datetime import datetime, timedelta


@python_2_unicode_compatible
class Departamento(TimeStampedModel):
    """ modelo para regiones de un país"""

    name = models.CharField('nombre', max_length=120)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Provincia(TimeStampedModel):
    """ modelo para provincias de Departamento"""

    name = models.CharField('nombre', max_length=120)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Distrito(TimeStampedModel):
    """ modelo para distrito de Provincia"""

    name = models.CharField('nombre', max_length=120)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Distrito'
        verbose_name_plural = 'Distritos'
        ordering = ['name']

    def __str__(self):
        return self.name
