from django.db import models

# Create your models here.
from utilisateur.models import Utilisateur


class Agents(models.Model):
    sexe_option = [('m', 'Masculin'), ('f', 'Féminin')]
    direction_option = [('DAGE', 'DAGE'), ('DFPT', 'DFPT'), ('PEJA', 'PEJA'), ('CI', 'Cellule Informatique'), ('CG', 'Cellule Genre')]
    agent_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(verbose_name='Prénom', blank=False, max_length=100)
    last_name = models.CharField(verbose_name='Nom de famille', blank=False, max_length=100)
    email_institutionnel = models.EmailField(verbose_name='Email Institutionnel', blank=False, unique=True, max_length=100)
    sexe = models.CharField(choices=sexe_option, verbose_name='Sexe', blank=False, max_length=100)
    tel1 = models.CharField(verbose_name='Numéro Téléphone', blank=False, unique=True, max_length=9)
    direction = models.CharField(choices=direction_option, blank=False, verbose_name="Direction", max_length=100)
    post_occupe = models.CharField(verbose_name='Poste Occupé', blank=False, max_length=100)
    autre_tel = models.CharField(verbose_name='Autre Numéro', blank=True, max_length=9)
    utilisateur_ref = models.ForeignKey(Utilisateur, verbose_name='Responsable', blank=False, on_delete=models.CASCADE, related_name='Utilisateur')