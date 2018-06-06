from django.contrib.auth.models import Permission, User
from django.db import models
from django.urls import reverse



class Album(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    artista = models.CharField(max_length=255, null=False)
    titulo = models.CharField(max_length=255, null=False)
    genero = models.CharField(max_length=255, null=False)
    capa = models.FileField()
    ano = models.IntegerField()
    favorito = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('music:detalhe', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s - %s (%i)' % (self.titulo, self.artista, self.ano)


class Musica(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255, null=False)
    favorita = models.BooleanField(default=False)
    arquivo_musica = models.FileField(default='')

    def get_absolute_url(self):
        return reverse('music:detalhe', kwargs={'id': self.pk})

    def __str__(self):
        return '%s' % self.nome


