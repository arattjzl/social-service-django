from django import forms
from .models import UnidadAcademica, ProgramaAcademico

class FormUnidadAcademica(forms.ModelForm):

    class Meta:
        model = UnidadAcademica
        fields = '__all__'  
        #fields = ['nombre'] 
        #exclude = ['nombre'] 

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control', 
                    'placeholder': 'UAIE',
                    }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Escribe una descripcion'
                }
            ),
        }

class FormProgramaAcademico(forms.ModelForm):

    class Meta:
        model = ProgramaAcademico
        fields = '__all__'

        widgets = {
            'unidad_academica': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control', 
                    'placeholder': 'UAIE',
                    }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Escribe una descripcion'
                }
            ),
        }

class FormFiltrosPrograma(forms.Form):
    nombre = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'}))
    descripcion = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Descripcion', 'class': 'form-control'}))
    unidad = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Unidad', 'class': 'form-control'}))

