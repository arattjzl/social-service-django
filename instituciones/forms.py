from django import forms
from .models import Instituciones

class FormInstituciones(forms.ModelForm):
    
    class Meta:
        model = Instituciones
        fields = '__all__'