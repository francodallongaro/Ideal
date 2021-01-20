from django import forms
from .models import *

class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ('nombre','tel','email')

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'tel': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
        }

class ClasificadoForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ('nombre','tel','email','mensaje')

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'tel': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'mensaje': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quisiera recibir más información.'})
        }