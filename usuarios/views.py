#!/usr/bin/python
# coding:utf-8
from django.shortcuts import render, redirect, render_to_response
from django.views.generic.base import View
from usuarios.forms import RegistrarUsuarioForm
from django.contrib.auth.models import User
from perfis.models import Perfil
from django.template.context import RequestContext

class RegistrarUsuarioView(View):

    template_name = 'registrar.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = RegistrarUsuarioForm(request.POST)
        if form.verificar_usuario():
            dados_form = form.data
            #create_user é um método da API User
            usuario_a_ser_cadastrado = User.objects.create_user(dados_form['nome'], dados_form['email'], dados_form['senha'])
            # é preciso associar o usuario a um Perfil
            perfil = Perfil(nome=dados_form['nome'],
                            email=dados_form['email'],
                            telefone=dados_form['telefone'],
                            areas_de_interesse=dados_form['areas_de_interesse'],
                            projetos_de_pesquisa=dados_form['projetos_de_pesquisa'],
                            usuario=usuario_a_ser_cadastrado)
            perfil.save()
            return redirect('index')

        # o form possui as informações dos erros no cadastro
        return render(request, self.template_name, {'form' : form})

class SocialAuthView(View):

    template_name = 'autenticar.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
       context = RequestContext(request,
                               {'request': request,
                                'user': request.user})
       return render_to_response('home.html',
                                 context_instance=context)
