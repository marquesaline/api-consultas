from datetime import datetime
from rest_framework import serializers, fields

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

    data_consulta = fields.DateField(input_formats=['%d-%m-%Y'])

    def validate(self, data):
        if datetime.now().date() > data['data_consulta']:
            raise serializers.ValidationError({
                'data_consulta': 'A data da consulta deve ser posterior ou igual a data atual'
            })
        
        if data['profissional'] is None:
            raise serializers.ValidationError({
                'profissional': 'Informe um id válido do profissional para a consulta'
            })
        return data

    class Meta:
        model = Consulta
        fields = (
            'id',
            'paciente',
            'nome_social',
            'profissional',
            'data_consulta'
        )