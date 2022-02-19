from django import forms

from portal.models import Noticia, Login


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        exclude = ()

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'assunto': forms.Textarea(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class Cadastra(forms.ModelForm):
    class Meta:
        model = Login
        exclude = ('senha',)

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
        }


class CadastraUser(forms.ModelForm):
    class Meta:
        model = Login
        exclude = ('tipo',)

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


