#!/usr/bin/python
# coding:utf-8
from django import forms
from django.contrib.auth.models import User # Permite que o banco autentique o usuário

class RegistrarUsuarioForm(forms.Form):
    nome = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    senha = forms.CharField(required=True)
    telefone = forms.CharField(required=True)
    areas_de_interesse = forms.CharField(required=True)
    projetos_de_pesquisa = forms.CharField(required=True)

    def verificar_usuario(self):
        is_valido = True
        if not super(RegistrarUsuarioForm, self).is_valid():
            self.adicionar_erro('Verifique os dados informados')
            is_valido = False

        usuario = User.objects.filter(username=self.data['nome']).exists()

        if usuario:
            self.adicionar_erro('Usuário já existente')
            is_valido = False

        return is_valido

    def adicionar_erro(self, mensagem):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(mensagem)
