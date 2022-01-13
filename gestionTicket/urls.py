"""gestionTicket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

from agents.views import listagent, saveagent, updateagent, rechercheragent, liste_attribution_agent, list_comptable, \
    connexionuser, index_base
from gestionTicket.views import index

urlpatterns = [
    path('', index, name='index'),
    path('accueil', index_base, name='accueil_base'),
    path('personnels', listagent, name='listagent'),
    path('saveAgent', saveagent, name='saveagent'),
    path('connexion', connexionuser, name='connexionuser'),
    path('personnels/<int:pk>', updateagent, name='updateAgent'),
    path('personnels/journal/<int:pk>', liste_attribution_agent, name='journal'),
    path('rechercher', rechercheragent, name='rechercheragent'),
    path('administration/', admin.site.urls),
    path('agents/', include('agents.urls')),
    path('comptables', list_comptable, name='list-comptable'),
]
