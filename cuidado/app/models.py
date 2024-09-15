from django.db import models

# Create your models here.
class Tarefa(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.CharField(max_length=150)
    enfermeira = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)