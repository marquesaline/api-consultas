from django.contrib import admin

from consultas.models import Profissional, Consulta


@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome',
        'nome_social',
        'especialidade'
    ]

    list_filter = (
        ('id', admin.AllValuesFieldListFilter),
        ('especialidade', admin.AllValuesFieldListFilter)
    )

    search_fields = (
        'id',
        'nome',
        'nome_social',
        'especialidade'
    )


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'paciente',
        'nome_social',
        'profissional',
        'data_consulta'
    ]

    search_fields = (
        'id',
        'paciente',
        'nome_social',
        'profissional',
        'data_consulta'
    )

    autocomplete_fields = ['profissional']

    list_filter = (
        ('id', admin.AllValuesFieldListFilter),
        ('profissional', admin.AllValuesFieldListFilter)
    )


