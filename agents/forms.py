from django import forms

from agents.models import Agents


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