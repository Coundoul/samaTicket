from datetime import datetime

from django.db import models

# Create your models here.
from agents.models import Agents
from utilisateur.models import Utilisateur


class Attribution(models.Model):
    attribution_id = models.BigAutoField(primary_key=True)
    nbr_ticket = models.IntegerField(verbose_name='Nombre de Tickets Recus :', blank=False)
    current_date = models.DateTimeField(verbose_name='Date Attribution', default=datetime.today(), blank=True)
    date_rendez_vous = models.DateTimeField(verbose_name='Date Rendez-vous', blank=False)
    agent = models.ForeignKey(Agents, verbose_name="Agents", on_delete=models.CASCADE, blank=False)
    utilisateur_at_ref = models.ForeignKey(Utilisateur, verbose_name="Utilisateur", blank=False, on_delete=models.CASCADE)