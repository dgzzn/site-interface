from django.db import models


class Album(models.Model):
    artista = models.CharField(max_length=255, null=False)
    titulo = models.CharField(max_length=255, null=False)
    genero = models.CharField(max_length=255, null=False)
    capa = models.CharField(max_length=255)
    ano = models.IntegerField()
    favorito = models.BooleanField(default=False)

    def __str__(self):
        return '%s - %s (%i)'%(self.titulo, self.artista, self.ano)


class Musica(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255, null=False)
    favorita = models.BooleanField(default=False)

    def __str__(self):
        return '%s'%self.nome


