#!/usr/bin/python
# coding:utf-8
from django.db import models
from abc import ABCMeta, abstractmethod
from django.contrib.auth.models import User

class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    areas_de_interesse = models.CharField(max_length=255, null=False)
    projetos_de_pesquisa = models.CharField(max_length=255, null=False)
    """perfil se relaciona com si mesmo numa relação
    muitos para muitos"""
    contatos = models.ManyToManyField('self')
    usuario = models.OneToOneField(User, related_name="perfil")

    @property
    def email(self):
        return self.usuario.email

    def convidar(self, perfil_convidado):
        convite = Convite.objects.create()
        convite.criar_convite(solicitante=self, convidado=perfil_convidado)


"""# Observer (Abstrato)
class Observer():
    __metaclass__ = ABCMeta

    @abstractmethod
    def update_status(self):
        pass"""


# Observer concreto
class ConviteObserver(models.Model):

    convite = models.OneToOneField('Convite')
    _CONVITE_ACEITO = "Stauts : Aceito"
    _CONVITE_AGUARDANDO = "Status: Aguardando resposta"

    def update_status(self, status):
        if status == _CONVITE_AGUARDANDO:
            self.convite.notificar(self.convite.convidado)
        elif status == _CONVITE_ACEITO:
            self.convite.notificar(self.convite.solicitante)


# Subject
class Convite(models.Model):
    """relacionamento bidirecional usando um parâmetro
    a mais no models.ForeignKey: o related_name"""
    solicitante = models.ForeignKey(Perfil, related_name='convites_feitos')
    convidado = models.ForeignKey(Perfil, related_name='convites_recebidos')
    observer = models.ForeignKey('ConviteObserver', related_name='+', default="")

    def criar_convite(self, solicitante, convidado):
        self.solicitante = solicitante
        self.convidado = convidado
        self.observer = ConviteObserver.objects.create()
        self.observer.convite = self
        self.observer.update_status("Status: Aguardando resposta")
        self.save()

    def aceitar_convite(self):
        self.convidado.contatos.add(self.solicitante)
        self.solicitante.contatos.add(self.convidado)
        self.observer.update_status("Status: Aceito")
        # deletar o convite após o convite ser aceito
        self.delete()

    def notificar(self, perfil):
        pass
