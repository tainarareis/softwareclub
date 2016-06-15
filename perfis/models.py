#!/usr/bin/python
# coding:utf-8
from django.db import models
from abc import ABCMeta, abstractmethod


class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    nome_empresa = models.CharField(max_length=255, null=False)
    """perfil se relaciona com si mesmo numa relação
    muitos para muitos"""
    contatos = models.ManyToManyField('self')
    provider = models.ForeignKey(NotificationCenter)

    def convidar(self, perfil_convidado):
        convite = Convite()
        convite.criar_convite(solicitante=self, convidado=perfil_convidado)
        convite.save()
        # self.subscribe(resultado_convite)

    def subscribe(self, categoria):
        self.provider.subscribe(categoria)


# Subject
class Convite(models.Model):
    """relacionamento bidirecional usando um parâmetro
    a mais no models.ForeignKey: o related_name"""
    solicitante = models.ForeignKey(Perfil, related_name='convites_feitos')
    convidado = models.ForeignKey(Perfil, related_name='convites_recebidos')
    observer = models.ForeignKey(ConviteObserver)

    def criar_convite(self, solicitante, convidado):
        self.solicitante = solicitante
        self.convidado = convidado
        self.observer.update_status("Status: Aguardando resposta")

    def aceitar_convite(self):
        self.convidado.contatos.add(self.solicitante)
        self.solicitante.contatos.add(self.convidado)
        self.observer.update_status("Status: Aceito")
        # deletar o convite após o convite ser aceito
        self.delete()


# Observer concreto
class ConviteObserver(Observer):

    convite = models.ForeignKey(Convite)
    _CONVITE_ACEITO = "Stauts : Aceito"
    _CONVITE_AGUARDANDO = "Status: Aguardando resposta"

    def update_status(self, status):
        if status == _CONVITE_AGUARDANDO:
            self.notificar(convite.convidado)
        else if status == _CONVITE_ACEITO:
            self.notificar(convite.solicitante)

    def notificar(self, perfil):
        pass


# Observer (Abstrato)
class Observer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def update_status(self):
        pass
