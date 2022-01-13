from django.urls import path

from agents.views import index, listagent, saveagent, deleteagent, updateagent, rechercheragent, \
    liste_attribution_agent, list_comptable, index_base, connexionuser

app_name = 'agent'

urlpatterns = [
    path('', index, name='accueil'),
    path('accueil', index_base, name='accueil_base'),
    path('personnels', listagent, name='list-agent'),
    path('connexion', connexionuser, name='connexionuser'),
    path('comptables', list_comptable, name='list-comptable'),
    path('saveAgent', saveagent, name='saveagent'),
    path('personnels/<int:pk>/', updateagent, name='updateAgent'),
    path('personnels/<int:pk>/', deleteagent, name='deleteAgent'),
    path('rechercher', rechercheragent, name='rechercheragent'),
    path('personnels/journal/<int:pk>', liste_attribution_agent, name='journal'),
]