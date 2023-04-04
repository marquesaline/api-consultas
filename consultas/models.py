from django.db import models


class BaseModel(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profissional(BaseModel):
    nome = models.CharField(max_length=100, blank=False, verbose_name='Nome')
    nome_social = models.CharField(max_length=100, blank=True, verbose_name='Nome social do profissional')
    especialidade = models.CharField(max_length=100, blank=True, verbose_name='Especialidade')

    class Meta:
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissionais'

    def __str__(self):
        nome = self.nome_social if self.nome_social else self.nome
        return f'{nome} - {self.especialidade}'

class Consulta(BaseModel):
    paciente = models.CharField(max_length=100, blank=False, verbose_name='Nome do paciente')
    nome_social = models.CharField(max_length=100, blank=True, verbose_name='Nome social do paciente')
    data_consulta = models.DateField(blank=False, verbose_name='Data da consulta')
    profissional = models.ForeignKey(Profissional, related_name='profissional', verbose_name='Nome do profissional', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'

