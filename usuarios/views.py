from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256

def login(request) :
  return render(request, 'login.html')

def cadastro(request):
  status = request.GET.get('status')
  return render(request, 'cadastro.html', {'status: status'})

def valida_cadastro(request) :
  nome = request.POST.get('nome')
  senha = request.POST.get('senha')
  email = request.POST.get('email')
  
   
  usuario = Usuario.objects.filter(email = email)
  
  if len (nome.strip()) == 0 or len(email.strip()) ==0:
    return redirect('auth/Cadastro/?status=1')
  
  if len(senha) < 8:
    return redirect('auth/Cadastro/?status=2')
  
  if len(usuario) > 0 :
    return redirect('auth/Cadastro/?status=3')
  
  try:
     senha = sha256(senha.encode()).hexdigest()
     usuario = Usuario(nome = nome, senha = senha, email = email)
     usuario.save()
     
     return redirect('auth/Cadastro/?status=0')
  
  except:
    return redirect('auth/Cadastro/?status=4') 
  
  
  
  
  
  return HttpResponse()