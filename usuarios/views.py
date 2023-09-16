from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario

def login(request) :
  return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def valida_cadastro(request) :
  nome = request.POST.get('nome')
  senha = request.POST.get('senha')
  email = request.POST.get('email')
  
  usuario = Usuario(nome = nome, senha = senha, email = email)
  usuario.save()
  
  
  
  return HttpResponse()