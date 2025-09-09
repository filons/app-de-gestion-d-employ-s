from django import forms
from .models import Employe

class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['nom', 'email', 'poste', 'salaire']
        widgets = {
            'nom': forms.TextInput(attrs={
                'class':'input w-full',
                'placeholder': 'Nom de l\'employé'
                }),
            'email': forms.EmailInput(attrs={
                'class':'input w-full',
                'placeholder': 'Email de l\'employé'
                }),
            'poste': forms.TextInput(attrs={
                'class':'input w-full',
                'placeholder': 'Poste de l\'employé'
                }),
            'salaire': forms.NumberInput(attrs={
                'class':'input w-full',
                'placeholder': 'Salaire de l\'employé'
                }),
        }