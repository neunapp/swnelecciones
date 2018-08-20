# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify
from django.conf import settings
# third-party
from model_utils.models import TimeStampedModel
from datetime import datetime, timedelta

#models local
from applications.home.models import Departamento, Provincia, Distrito
# managers
from .managers import (
    VotoRegionManager,
    VotoDistritoManager,
    VotoConsejeroManager,
    VotoProvinciaManager
)


@python_2_unicode_compatible
class PartidoPolitico(TimeStampedModel):
    """ modelo para partido politico"""

    name = models.CharField('nombre corto', max_length=120)
    name_large = models.CharField('nombre largo', max_length=200)
    image = models.ImageField(upload_to="partido", blank=True, null=True)

    class Meta:
        verbose_name = 'Partido Politico'
        verbose_name_plural = 'Partidos Politicos'
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class CandidatoDepartamento(TimeStampedModel):
    """ modelo para registro de candidato departamental """

    partido = models.ForeignKey(PartidoPolitico, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    candidato = models.CharField('nombre candidato', max_length=200, blank=True)
    foto = models.ImageField(upload_to="regional",  blank=True, null=True)

    class Meta:
        verbose_name = 'Candidato Departamental'
        verbose_name_plural = 'Candidatos Departamentales'
        ordering = ['partido__name']

    def __str__(self):
        return self.departamento.name + '-' + self.partido.name


@python_2_unicode_compatible
class ConsejeroDepartamento(TimeStampedModel):
    """ modelo para registro de candidato departamental """

    partido = models.ForeignKey(PartidoPolitico, on_delete=models.CASCADE)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    candidato = models.CharField('nombre candidato', max_length=200, blank=True)
    foto = models.ImageField(upload_to="consejero",  blank=True, null=True)

    class Meta:
        verbose_name = 'Consejero departamental'
        verbose_name_plural = 'Consejeros departamentales'
        ordering = ['partido__name']

    def __str__(self):
        return self.departamento.name + '-' + self.partido.name


@python_2_unicode_compatible
class CandidatoProvincia(TimeStampedModel):
    """ modelo para registro de candidato provincial """

    partido = models.ForeignKey(PartidoPolitico, on_delete=models.CASCADE)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    candidato = models.CharField('nombre candidato', max_length=200, blank=True)
    foto = models.ImageField(upload_to="provincia",  blank=True, null=True)

    class Meta:
        verbose_name = 'Candidato Provincial'
        verbose_name_plural = 'Candidatos Provinciales'
        ordering = ['partido__name']

    def __str__(self):
        return self.provincia.name + '-' + self.partido.name


@python_2_unicode_compatible
class CandidatoDistrito(TimeStampedModel):
    """ modelo para registro de candidato distrital """

    partido = models.ForeignKey(PartidoPolitico, on_delete=models.CASCADE)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    candidato = models.CharField('nombre candidato', max_length=200, blank=True)
    foto = models.ImageField(upload_to="distrito",  blank=True, null=True)

    class Meta:
        verbose_name = 'Candidato Distrital'
        verbose_name_plural = 'Candidatos Distritales'
        ordering = ['partido__name']

    def __str__(self):
        return self.distrito.name + '-' + self.partido.name


@python_2_unicode_compatible
class VotoRegion(TimeStampedModel):
    """ modelo para votos de candidatos regionales"""

    electo = models.ForeignKey(CandidatoDepartamento, on_delete=models.CASCADE)
    ippc = models.CharField(max_length=30)
    date = models.DateField('Fecha')

    objects = VotoRegionManager()

    class Meta:
        unique_together = ('ippc', 'date')
        verbose_name = 'Votos Presidente Regional'
        verbose_name_plural = 'Votos Presidente Regional'
        ordering = ['date']

    def __str__(self):
        return self.electo.partido.name


@python_2_unicode_compatible
class VotoConsejero(TimeStampedModel):
    """ modelo para votos de candidatos regionales"""

    electo = models.ForeignKey(ConsejeroDepartamento, on_delete=models.CASCADE)
    ippc = models.CharField(max_length=30)
    date = models.DateField('Fecha')

    objects = VotoConsejeroManager()

    class Meta:
        unique_together = ('ippc', 'date')
        verbose_name = 'Votos Consejero'
        verbose_name_plural = 'Votos Consejero'
        ordering = ['date']

    def __str__(self):
        return self.electo.partido.name


@python_2_unicode_compatible
class VotoProvincia(TimeStampedModel):
    """ modelo para votos de candidatos regionales"""

    electo = models.ForeignKey(CandidatoProvincia, on_delete=models.CASCADE)
    ippc = models.CharField(max_length=30)
    date = models.DateField('Fecha')

    objects = VotoProvinciaManager()

    class Meta:
        unique_together = ('ippc', 'date')
        verbose_name = 'Votos Provincia'
        verbose_name_plural = 'Votos Provincia'
        ordering = ['date']

    def __str__(self):
        return self.electo.partido.name


@python_2_unicode_compatible
class VotoDistrito(TimeStampedModel):
    """ modelo para votos de candidatos regionales"""

    electo = models.ForeignKey(CandidatoDistrito, on_delete=models.CASCADE)
    ippc = models.CharField(max_length=30)
    date = models.DateField('Fecha')

    objects = VotoDistritoManager()

    class Meta:
        unique_together = ('ippc', 'date')
        verbose_name = 'Votos Distrito'
        verbose_name_plural = 'Votos Distrito'
        ordering = ['date']

    def __str__(self):
        return self.electo.partido.name
