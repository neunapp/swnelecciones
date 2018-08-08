from django.contrib import admin

# Register your models here.
from .models import (
    PartidoPolitico,
    CandidatoDepartamento,
    ConsejeroDepartamento,
    CandidatoProvincia,
    CandidatoDistrito,
    VotoRegion,
    VotoConsejero,
    VotoProvincia,
    VotoDistrito
)

class CandidatoDepartamentoAdmin(admin.ModelAdmin):

    list_display = (
        'partido',
        'departamento',
        'candidato',
    )
    #
    search_fields = ('candidato',)
    list_filter = ('departamento',)


class ConsejeroAdmin(admin.ModelAdmin):

    list_display = (
        'partido',
        'departamento',
        'candidato',
    )
    #
    search_fields = ('candidato',)
    list_filter = ('departamento',)


class ProvinciaAdmin(admin.ModelAdmin):

    list_display = (
        'partido',
        'provincia',
        'candidato',
    )
    #
    search_fields = ('candidato',)
    list_filter = ('provincia',)


class DistritoAdmin(admin.ModelAdmin):

    list_display = (
        'partido',
        'distrito',
        'candidato',
    )
    #
    search_fields = ('candidato',)
    list_filter = ('distrito',)


admin.site.register(PartidoPolitico)
admin.site.register(CandidatoDepartamento, CandidatoDepartamentoAdmin)
admin.site.register(ConsejeroDepartamento, ConsejeroAdmin)
admin.site.register(CandidatoProvincia, ProvinciaAdmin)
admin.site.register(CandidatoDistrito, DistritoAdmin)
admin.site.register(VotoRegion)
admin.site.register(VotoConsejero)
admin.site.register(VotoProvincia)
admin.site.register(VotoDistrito)
