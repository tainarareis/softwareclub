#!/usr/bin/python
# coding:utf-8
from django.shortcuts import render, redirect
from perfis.models import Perfil, Convite


def index(request):
    return render(request, 'index.html', {
        'perfis': Perfil.objects.all(),
        'perfil_logado': get_perfil_logado(request)})


def homepage(request):
    return render(request, 'homepage.html')


def busca(request):
    return render(request, 'busca.html')


def exibir(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    is_contato = perfil in perfil_logado.contatos.all()
    if perfil == perfil_logado:
        proprio_perfil = True
    else:
        proprio_perfil = False
    """render: retorna o mesmo request, o nome do template e um
    dicionário com os dados que se pretende disponibilizar no template """
    return render(request, 'perfil.html', {"perfil": perfil, "is_contato": is_contato, "proprio_perfil" : proprio_perfil})


def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    """redirect troca o request, logo não se pode disponibilizar
    nada para o template."""
    return redirect('index')


def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')

def get_perfil_logado(request):
    return Perfil.objects.get(id=1)
