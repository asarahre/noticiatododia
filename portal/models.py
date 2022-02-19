from django.db import models


# Create your models here.


class Login(models.Model):

    TIPOS = [
        ('ADM', "Adm"),
        ('NORMAL', "Normal")
    ]

    nome = models.CharField(max_length=150)
    email = models.EmailField(null=True, blank=True)
    senha = models.CharField(max_length=150)
    tipo = models.CharField(max_length=50, choices=TIPOS, default='NORMAL')


class Noticia(models.Model):
    autor = models.CharField(max_length=150)
    titulo = models.CharField(max_length=255)
    assunto = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='img/noticia')
    data = models.DateField()


class Comentario(models.Model):
    comentarios = models.TextField(default='')
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, null=True, blank=True)
    usuario = models.ForeignKey(Login, on_delete=models.CASCADE, null=True, blank=True)
