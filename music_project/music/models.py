from django.db import models

# Create your models here.

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(max_length=200)
    fundacao = models.DateField(auto_now=False, auto_now_add=False)
    
    estilo = models.ForeignKey(
        'EstiloMusical',
        on_delete=models.CASCADE,
    )
        
    def __str__(self):
        return self.nome

class Musico(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.DecimalField(max_digits=20, decimal_places=0)
    bandas = models.ManyToManyField(Banda)

    def __str__(self):
        return self.nome
        
class EstiloMusical(models.Model):
    nome = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome
