from django import forms
from .models import *


class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields= '__all__'
        widgets = {
            'nit': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'libros': forms.SelectMultiple(attrs={'class':'selectpicker', 'title':'Escoger Libros', 'data-size':'3'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'sitioweb': forms.TextInput(attrs={'class':'form-control'}),
         }

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'autor': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'selectpicker'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'paginas': forms.TextInput(attrs={'class':'form-control'}),
            'fragmento': forms.Textarea(attrs={'class':'form-control'}),
        }
    
