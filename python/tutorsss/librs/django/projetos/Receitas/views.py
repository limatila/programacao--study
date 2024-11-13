from django.shortcuts import render
from .models import Receita

from tests.fakeDataTests.Receitas.fakes import main as genFakeData
from random import randint

# Create your views here.

def HOME(request):
    receitaQueried = Receita.objects.get(idPage=1)

    return render(request, "pages/home-receitas.html",
                  context={
                      "pageDetails": {"isMainMenu": True,
                                      "isDetailMenu": False},
                      "receitas": [ genFakeData(num) for num in range(5) ] + [receitaQueried], #* gera 5 fakes pra uso, e adiciona a última também!
                      #? receitas devem ser pegues do DB, categorizando por número de cliques
                    },
                  content_type="text/html")

def RECEITA(request, idReceita):
    return render(request, "pages/receita.html/",
                  context={
                      "pageDetails": {"isMainMenu": False,
                                      "isDetailMenu": True},
                      "receita": genFakeData(idReceita), 
                      #? receita deve ser peque do DB, onde idReceita deve ser o ID PK 
                    },
                  content_type="text/html")

def randomRECEITA(request): # Para botão 'Me mostre uma nova!'
    randomID = randint(0, 5)
    return RECEITA(request, randomID)