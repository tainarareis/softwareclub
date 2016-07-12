#!/usr/bin/python
# coding:utf-8
from django.db import models
from abc import ABCMeta, abstractmethod
from django.contrib.auth.models import User

class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=True)
    areas_de_interesse = models.CharField(max_length=255, null=True)
    projetos_de_pesquisa = models.CharField(max_length=255, null=True)
    """perfil se relaciona com si mesmo numa relação
    muitos para muitos"""
    contatos = models.ManyToManyField('self')
    usuario = models.OneToOneField(User, related_name="perfil")

    @property
    def email(self):
        self.usuario.email

    def convidar(self, perfil_convidado):
        Convite(solicitante=self, convidado=perfil_convidado).save()


"""# Observer (Abstrato)
class Observer():
    __metaclass__ = ABCMeta

    @abstractmethod
    def update_status(self):
        pass"""


"""# Observer concreto
class ConviteObserver(models.Model):

    convite = models.ForeignKey('Convite')
    #publisher = models.ForeignKey('Publisher', related_name="publishers")

    #CONVITE_ACEITO = "Stauts : Aceito"
    #CONVITE_AGUARDANDO = "Status: Aguardando resposta"

    @classmethod
    def create(self, convite):
        observer = ConviteObserver(convite=convite)
        return observer

    def update_status(self, status):
        if status == "Stauts : Aceito":
            self.notificar_convite_aceito(self.convite.solicitante)
        elif status == "Status: Aguardando resposta":
            self.notificar_convite_aguardando(self.convite.convidado)

    def notificar_convite_aceito(self, perfil):
        notificacao = "O convite a " + self.convite.solicitante.nome + " foi aceito."
        return notificacao

    def notificar_convite_aguardando(self, perfil):
        notificacao = perfil.nome +" te enviou um convite."
        return notificacao
"""
"""
class Publisher(models.Model):

    def notificar_convite_aceito(self, perfil):
        notificacao = "O convite a " + perfil.nome + " foi aceito."
        return notificacao

    def notificar_convite_aguardando(self, perfil):
        notificacao = perfil.nome +" te enviou um convite."
        return notificacao
"""

# Subject
class Convite(models.Model):
    """relacionamento bidirecional usando um parâmetro
    a mais no models.ForeignKey: o related_name"""
    solicitante = models.ForeignKey(Perfil, related_name='convites_feitos')
    convidado = models.ForeignKey(Perfil, related_name='convites_recebidos')
    #observer = models.ForeignKey(ConviteObserver, related_name='observers')

    @classmethod
    def create(self, solicitante, convidado):
        convite = Convite(solicitante=solicitante, convidado=convidado)
        #self.observer = ConviteObserver.create(convite)
        #convite.notificar_observer("Status: Aguardando resposta")

    """def notificar_observer(self, status):
        self.observer.update_status(status)"""

    def aceitar_convite(self):
        self.convidado.contatos.add(self.solicitante)
        self.solicitante.contatos.add(self.convidado)
        #convite.notificar_observer("Status: Aceito")
        # deletar o convite após o convite ser aceito
        self.delete()
