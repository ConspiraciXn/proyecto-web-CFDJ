from django.db import models
from django.db.models.base import Model

# Create your models here.
class Categoria(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    nombre = models.CharField(max_length=120)

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150)
    lead = models.CharField(max_length=150)
    cuerpo = models.CharField(max_length=3000)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='imgNoticia', default='imgNoticia/noDisponible.png')
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    activo = models.BooleanField(default=False)
    comentario = models.TextField(default='-')
    periodista = models.TextField(default='-')

    def __str__(self):
        return self.titulo

class Galeria(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='galeriaNoticia')
    Noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)

    def __str__(self):
        return "Numero: " + str(self.id)
