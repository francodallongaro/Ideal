from django import forms
from .models import Usuario

# class ContactoForm(forms.ModelForm):
    
#     class Meta:
#         model = Contacto
#         fields = ('nombre','tel','email')

#         widgets = {
#             'nombre': forms.TextInput(attrs={'class': 'form-control'}),
#             'tel': forms.NumberInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'})
#         }

class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ('nombre','tel','email', 'estado')

        # widgets = {
        #     'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        #     'tel': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'estado': forms.(attrs={'class': 'form-control'})
        # }