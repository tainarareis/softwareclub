#!/usr/bin/python
# coding:utf-8
from django.shortcuts import render, redirect
from social.pipeline.partial import partial
from importlib import import_module
import pprint

def get_backend_info(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        #user = user.get_profile()
        #usuario_a_ser_cadastrado = User.objects.create_user(username=response.get('name'), email=response.get('email'))
        #usuario_a_ser_cadastrado.nome = response.get('name')
        #usuario_a_ser_cadastrado.email = response.get('email')
        #print ("usuario_a_ser_cadastrado")
        # eh preciso associar o usuario a um Perfil
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(response)
        nome = str(response.get('name'))
        email = str(response.get('email'))
        pp.pprint(nome)
        pp.pprint(email)
        return redirect('solicitar_completar_cadastro', nome, email)


"""
@partial
def require_email(strategy, details, user=None, is_new=False, *args, **kwargs):
    if kwargs.get('ajax') or user and user.email:
        return
    elif is_new and not details.get('email'):
        email = strategy.request_data().get('email')
        if email:
            details['email'] = email
        else:
            return redirect('require_email')

def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        profile = user.get_profile()
        if profile is None:
            profile = Profile(user_id=user.id)
        profile.gender = response.get('gender')
        profile.link = response.get('link')
        profile.timezone = response.get('timezone')
        profile.save()

def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        profile = user.get_profile()
        if profile is None:
            profile = Profile(user_id=user.id)
        profile.gender = response.get('gender')
        profile.link = response.get('link')
        profile.timezone = response.get('timezone')
        profile.save()
"""
