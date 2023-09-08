from django.db import models

class Livros(models.Model) :
  titulo = models.CharField(max_length = 100)
  autor = models.CharField(max_length = 40)
  co_autor = models.CharField(max_length = 40)
  volume = models.CharField(max_length = 10)
  genero = models.CharField(max_length = 100)
  data_cadastro = models.DateField()
  emprestado = models.BooleanField(default=False)
  nome_emprestado = models.CharField(max_length = 100)
  data_emprestimo = models.DateTimeField()
  data_devolucao = models.DateField()
  
  class Meta:
    verbose_name="Livro"
  