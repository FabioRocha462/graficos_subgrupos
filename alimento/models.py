from django.db import models
from categoria.models import Categoria
# Create your models here.
class Alimento(models.Model):
    nome = models.CharField(max_length = 255)
    valor = models.FloatField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome