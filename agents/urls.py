from django.urls import path

from agents.views import index, listagent, saveagent, deleteagent, updateagent, rechercheragent, \
    liste_attribution_agent, list_comptable, index_base, connexionuser, active_compte, rechercher_comptable

app_name = 'mefpai'

urlpatterns = [
    path('', index_base, name='accueil'),
    path('accueil', index_base, name='accueil'),
    path('personnels', listagent, name='list-agent'),
    path('login', connexionuser, name='connexionuser'),
    path('comptables', list_comptable, name='list-comptable'),
    path('rechercher/comptable', rechercher_comptable, name='rechercher_comptable'),
    path('comptables/compte/<int:pk>/', active_compte, name='active_compte'),
    path('comptables/journal/<int:pk>', liste_attribution_agent, name='journal'),
    path('saveAgent', saveagent, name='saveagent'),
    path('personnels/<int:pk>/', updateagent, name='updateAgent'),
    path('personnels/<int:pk>/', deleteagent, name='deleteAgent'),
    path('rechercher', rechercheragent, name='rechercheragent'),
    path('personnels/journal/<int:pk>', liste_attribution_agent, name='journal'),
]