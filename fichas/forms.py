from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Personagem


class PersonagemForm(forms.ModelForm):
    class Meta:
        model = Personagem
        fields = [
            'nome_personagem',
            'nome_jogador',
            'classe',
            'raca',
            'nivel',
            'vida',
            'mana',
            'forca',
            'destreza',
            'constituicao',
            'inteligencia',
            'sabedoria',
            'carisma',
            'avatar',
        ]


class CadastroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2'
        ]