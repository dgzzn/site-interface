from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

from .models import Album, Musica


class UserForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'senha']


class UserLoginForm(forms.Form):
    usuario = forms.CharField()
    senha = forms.CharField(widget=forms.PasswordInput)


class MusicaForm(forms.ModelForm):

    class Meta:
        model = Musica
        fields = ('nome', 'arquivo_musica')


"""
class AlbumForm(ModelForm):
    class Meta:
        model = Album
        """
