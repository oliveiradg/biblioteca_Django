from django.db import models
from datetime import date

class Livros(models.Model) :
  titulo = models.CharField(max_length = 100)
  autor = models.CharField(max_length = 40)
  co_autor = models.CharField(max_length = 40, blank= True)
  volume = models.CharField(max_length = 10, blank=True, null=True)
  genero = models.CharField(max_length = 100)
  data_cadastro = models.DateField(default=date.today)
  emprestado = models.BooleanField(default=False)
  nome_emprestado = models.CharField(max_length = 100, blank= True, null=True)
  data_emprestimo = models.DateTimeField(blank= True, null=True)
  data_devolucao = models.DateTimeField(blank= True, null=True)
  tempo_duracao = models.DateField( blank= True, null=True)
  
  class Meta :
    
    verbose_name = 'Livro'
  
  def __str__(self) :
    return self.titulo
  
  
  
    
  
  
  
  
  
  