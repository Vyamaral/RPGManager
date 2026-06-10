from django.db import models
from django.contrib.auth.models import User


class Personagem(models.Model):

    usuario = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)

    nome_personagem = models.CharField(max_length=100)
    nome_jogador = models.CharField(max_length=100)

    classe = models.CharField(max_length=50)
    raca = models.CharField(max_length=50)

    nivel = models.IntegerField()

    vida = models.IntegerField()
    mana = models.IntegerField()

    forca = models.IntegerField()
    destreza = models.IntegerField()
    constituicao = models.IntegerField()
    inteligencia = models.IntegerField()
    sabedoria = models.IntegerField()
    carisma = models.IntegerField()

    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome_personagem