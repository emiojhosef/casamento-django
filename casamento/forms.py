from django.forms import ModelForm
from casamento.models import ListaPresente, Convidado
from django import forms

# Create the form class.
class ListaPresenteForm(ModelForm):
    class Meta:
        model = ListaPresente
        fields = ["foto", "nome", "preco"]

        widgets = {
            'foto': forms.FileInput(attrs={'class':'presente'}),
            'nome': forms.TextInput(attrs={'class':'presente'}),
            'preco': forms.TextInput(attrs={'class':'presente'}),
        }

class ConvidadoForms(forms.Form):
    nome = forms.CharField(
        max_length=100,
        label='Insira o nome do seu convite:',
        widget=forms.TextInput(attrs={
            'class': 'confirmacao-presenca-input',
        })
    )

class TelefoneForms(forms.Form):
    digito1 = forms.CharField(
        max_length=1,
        min_length=1,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'codigo-telefone',
            'maxlength': '1',
            'autocomplete': 'off',
            'inputmode': 'numeric',
            'pattern': '[0-9]*',
        })
    )

    digito2 = forms.CharField(
        max_length=1,
        min_length=1,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'codigo-telefone',
            'maxlength': '1',
            'autocomplete': 'off',
            'inputmode': 'numeric',
            'pattern': '[0-9]*',
        })
    )

    digito3 = forms.CharField(
        max_length=1,
        min_length=1,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'codigo-telefone',
            'maxlength': '1',
            'autocomplete': 'off',
            'inputmode': 'numeric',
            'pattern': '[0-9]*',
        })
    )

    digito4 = forms.CharField(
        max_length=1,
        min_length=1,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'codigo-telefone',
            'maxlength': '1',
            'autocomplete': 'off',
            'inputmode': 'numeric',
            'pattern': '[0-9]*',
        })
    )