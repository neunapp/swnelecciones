from django.db import models
from django.db.models import Count, F, Value, FloatField
# standard library
from datetime import timedelta, datetime

class VotoRegionManager(models.Manager):
    """
        procedimientos para tabla SOcial project
    """

    def lista_resultados_7(self, distrito):
        """Consulta para recuperar resultados ordenados"""
        hoy = datetime.now() # fecha de hoy
        date_end = hoy + timedelta(days=1)
        date_start = hoy - timedelta(days=7)
        # consulta de ultimos 7 dias
        consulta = self.filter(
            date__lte=date_end,
            date__gte=date_start,
            electo__departamento__pk=distrito.provincia.departamento.pk
        )
        # tamanio de poblacion
        poblacion = float(consulta.count())
        # agrupamos consulta
        resultados = consulta.values(
            'electo__partido__id',
            'electo__partido__name_large',
            'electo__partido__name',
            'electo__candidato',
            'electo__partido__image'
        ).annotate(
            votos=Count('ippc', output_field=FloatField()),
        ).annotate(
            porcentaje=F('votos')*100/poblacion,
        ).order_by('-porcentaje')
        return resultados


class VotoConsejeroManager(models.Manager):
    """
        procedimientos para tabla SOcial project
    """

    def lista_resultados_7(self, distrito):
        """Consulta para recuperar resultados ordenados"""
        hoy = datetime.now() # fecha de hoy
        date_end = hoy + timedelta(days=1)
        date_start = hoy - timedelta(days=7)
        # consulta de ultimos 7 dias
        consulta = self.filter(
            date__lte=date_end,
            date__gte=date_start,
            electo__provincia__pk=distrito.provincia.pk
        )
        # tamanio de poblacion
        poblacion = float(consulta.count())
        # agrupamos consulta
        resultados = consulta.values(
            'electo__partido__id',
            'electo__partido__name_large',
            'electo__partido__name',
            'electo__candidato',
            'electo__partido__image'
        ).annotate(
            votos=Count('ippc', output_field=FloatField()),
        ).annotate(
            porcentaje=F('votos')*100/poblacion,
        ).order_by('-porcentaje')
        return resultados


class VotoProvinciaManager(models.Manager):
    """
        procedimientos para tabla SOcial project
    """

    def lista_resultados_7(self, distrito):
        """Consulta para recuperar resultados ordenados"""
        hoy = datetime.now() # fecha de hoy
        date_end = hoy + timedelta(days=1)
        date_start = hoy - timedelta(days=7)
        # consulta de ultimos 7 dias
        consulta = self.filter(
            date__lte=date_end,
            date__gte=date_start,
            electo__provincia__pk=distrito.provincia.pk
        )
        # tamanio de poblacion
        poblacion = float(consulta.count())
        # agrupamos consulta
        resultados = consulta.values(
            'electo__partido__id',
            'electo__partido__name_large',
            'electo__partido__name',
            'electo__candidato',
            'electo__partido__image'
        ).annotate(
            votos=Count('ippc', output_field=FloatField()),
        ).annotate(
            porcentaje=F('votos')*100/poblacion,
        ).order_by('-porcentaje')
        return resultados


class VotoDistritoManager(models.Manager):
    """
        procedimientos para tabla SOcial project
    """

    def lista_resultados_7(self, distrito):
        """Consulta para recuperar resultados ordenados"""
        hoy = datetime.now() # fecha de hoy
        date_end = hoy + timedelta(days=1)
        date_start = hoy - timedelta(days=7)
        # consulta de ultimos 7 dias
        consulta = self.filter(
            date__lte=date_end,
            date__gte=date_start,
            electo__distrito__pk=distrito.pk
        )
        # tamanio de poblacion
        poblacion = float(consulta.count())
        # agrupamos consulta
        resultados = consulta.values(
            'electo__partido__id',
            'electo__partido__name_large',
            'electo__partido__name',
            'electo__distrito__name',
            'electo__candidato',
            'electo__partido__image'
        ).annotate(
            votos=Count('ippc', output_field=FloatField()),
        ).annotate(
            porcentaje=F('votos')*100/poblacion,
        ).order_by('-porcentaje')
        return resultados
