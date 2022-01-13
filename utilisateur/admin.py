from django.contrib import admin

# Register your models here.
from utilisateur.models import Utilisateur

admin.site.register(Utilisateur)
