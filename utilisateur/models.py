from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from orca.sound import args


class Utilisateur(User):
    utilisateur_id = models.BigAutoField(primary_key=True)
    sexe_option = [('m', 'Masculin'), ('f', 'Féminin')]
    role = [('AS', 'Admin Secondaire'), ('CP', 'Comptable Principale'), ('CS', 'Comptable Secondaire')]
    role_option = [('CP', 'Comptable Principale'), ('CS', 'Comptable Secondaire')]
    direction_option = [('DAGE', 'DAGE'), ('DFPT', 'DFPT'), ('PEJA', 'PEJA'), ('CI', 'Cellule Informatique'), ('CG', 'Cellule Genre')]
    sexe = models.CharField(blank=False, choices=sexe_option, max_length=100)
    tel1 = models.CharField(verbose_name='Numéro Téléphone', blank=False, unique=True, max_length=9)
    direction = models.CharField(blank=False, choices=direction_option, verbose_name="Direction", max_length=100)
    post_occupe = models.CharField(verbose_name='Poste Occupé', blank=False, max_length=100)
    autre_tel = models.CharField(verbose_name='Autre Numéro', blank=True, max_length=9)
    role = models.CharField(choices=role, verbose_name="Profile", blank=False, max_length=100)

    class Meta:
        verbose_name = "Utilisateur"