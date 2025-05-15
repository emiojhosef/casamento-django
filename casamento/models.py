from django.db import models
class ListaPresente(models.Model):
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    publicada = models.BooleanField(default=True)
    pix_link = models.URLField(max_length=500, blank=True)  # Novo campo
    def __str__(self):
        return self.nome
    
class Convidado(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    telefone = models.CharField(max_length=14)
    senha = models.CharField(max_length=4, unique=True)
    confirmado = models.BooleanField(default=False)
    confirmado_2 = models.BooleanField(default=False)
    def __str__(self):
        return self.nome

class MembroDaFamilia(models.Model):
    convidado = models.ForeignKey(Convidado, on_delete=models.CASCADE, related_name='familia')
    nome = models.CharField(max_length=200)
    confirmado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nome} (Família de {self.convidado.nome})"