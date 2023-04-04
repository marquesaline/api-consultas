from rest_framework import serializers

from consultas.models import Profissional, Consulta


class ProfissionalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profissional
        fields = (
            'id',
            'nome',
            'nome_social',
            'especialidade'
        )


class ConsultaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consulta
        fields = (
            'id',
            'paciente',
            'nome_social',
            'profissional',
            'data_consulta'
        )