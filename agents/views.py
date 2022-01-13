from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.
from agents.forms import AgentsForms
from agents.models import Agents
from django.http import JsonResponse

from attribution.models import Attribution
from utilisateur.models import Utilisateur
from django.contrib.auth import logout


def index(request):
    return render(request, 'accueil.html')


def index_base(request):
    return render(request, 'base.html')


def saveagent(request):
    if request.method == 'POST':
        form = AgentsForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('personnels')
    else:
        form = AgentsForms()
        agent = Agents.objects.all()
        return render(request, 'agent.html', {'agent': agent, 'form': form})


def listagent(request):
    form = AgentsForms()
    agent = Agents.objects.all()
    taille = len(agent)
    return render(request, 'agent.html', {'agent': agent, 'form': form, 'taille': taille})


def updateagent(request, pk):
    agent = Agents.objects.get(pk=pk)
    form = AgentsForms(instance=agent)

    if request.method == 'POST':
        form = AgentsForms(request.POST, instance=agent)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('personnels')
    return render(request, 'agent.html', {'agent': agent, 'form': form})


def rechercheragent(request):
    form = AgentsForms()
    try:
        if request.method == 'POST':
            email = request.POST['emailagent']
            agent = Agents.objects.get(email_institutionnel=email)
            nbr = 1
            return render(request, 'rechercher.html', {'agent': agent, 'form': form, 'nbr': nbr, 'email': email})
    except:
        agent = ''
        return render(request, 'rechercher.html', {'agent': agent, 'form': form, 'email': email})

    return HttpResponseRedirect('personnels')


def liste_attribution_agent(request, pk):
    if pk:
        form = AgentsForms()
        agent = Agents.objects.get(pk=pk)
        attribution = Attribution.objects.filter(agent=agent)
        return render(request, 'journal.html', {'agent': agent, 'attribution': attribution, 'form': form})
    return HttpResponseRedirect('personnels')


def list_comptable(request):
    form = AgentsForms()
    comptables = Utilisateur.objects.filter(role='CS')
    return render(request, 'comptables.html', {'comptables': comptables, 'form': form})


def deleteagent(request, pk):
    agent = Agents.objects.get(pk=pk)
    agent.objects.delete()
    return render(request, 'delete.html', {'agent': agent})


def connexionuser(request):
    return render(request, 'base.html')


def logout_view(request):
    logout(request)
