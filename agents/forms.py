from django import forms

from agents.models import Agents
from utilisateur.models import Utilisateur


class AgentsForms(forms.ModelForm):
    class Meta:
        sexe_option = [('m', 'Masculin'), ('f', 'Féminin')]
        model = Agents
        fields = ('first_name', 'last_name', 'email_institutionnel','sexe', 'direction', 'tel1', 'post_occupe', 'autre_tel', 'utilisateur_ref')

        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'from-control'}),
            'email_institutionnel': forms.TextInput(attrs={'class': 'from-control'}),
            'sexe': forms.Select(attrs={'class': 'form-control col-sm-2'}),
            'tel1': forms.TextInput(attrs={'class': 'from-control'}),
            'direction': forms.Select(attrs={'class': 'form-control col-sm-2'}),
            'post_occupe': forms.TextInput(attrs={'class': 'from-control'}),
            'autre_tel': forms.TextInput(attrs={'class': 'from-control'}),
            'utilisateur_ref': forms.Select(attrs={'class': 'form-control col-sm-2'})
        }


class UtilisateurForms(forms.ModelForm):
    class Meta:
        sexe_option = [('m', 'Masculin'), ('f', 'Féminin')]
        model = Utilisateur
        fields = ('first_name', 'last_name', 'username', 'password', 'groups','email', 'sexe', 'direction', 'tel1', 'post_occupe', 'is_active')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'from-control'}),
            'last_name': forms.TextInput(attrs={'class': 'from-control'}),
            'username': forms.TextInput(attrs={'class': 'from-control'}),
            'password': forms.TextInput(attrs={'class': 'from-control', 'type': 'password'}),
            'groups': forms.Select(attrs={'class': 'form-control col-sm-2'}),
            'email': forms.TextInput(attrs={'class': 'from-control'}),
            'sexe': forms.Select(attrs={'class': 'form-control col-sm-2'}),
            'tel1': forms.TextInput(attrs={'class': 'from-control'}),
            'direction': forms.Select(attrs={'class': 'form-control col-sm-2'}),
            'post_occupe': forms.TextInput(attrs={'class': 'from-control'}),
            'autre_tel': forms.TextInput(attrs={'class': 'from-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'from-control '}),
        }