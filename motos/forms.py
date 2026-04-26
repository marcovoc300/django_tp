from django import forms
from .models import Moto

class MotoForm(forms.ModelForm):
    class Meta:
        model = Moto
        fields = ['marca', 'modelo', 'descripcion', 'imagen']