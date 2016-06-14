#!/usr/bin/python
# coding:utf-8
from django.db import models


class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    nome_empresa = models.CharField(max_length=255, null=False)
    """perfil se relaciona com si mesmo numa relação
    muitos para muitos"""
    contatos = models.ManyToManyField('self')

    def convidar(self, perfil_convidado):
        Convite(solicitante=self, convidado=perfil_convidado).save()


class Convite(models.Model):
    """relacionamento bidirecional usando um parâmetro
    a mais no models.ForeignKey: o related_name"""
    solicitante = models.ForeignKey(Perfil, related_name='convites_feitos')
    convidado = models.ForeignKey(Perfil, related_name='convites_recebidos')

    def aceitar(self):
        self.convidado.contatos.add(self.solicitante)
        self.solicitante.contatos.add(self.convidado)
        # deletar o convite após o convite ser aceitar_convite
        self.delete()
