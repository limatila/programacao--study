from django.shortcuts import render

from .models import Receita
#test: from tests.fakeDataTests.Receitas.fakes import main as genFakeData

from random import randint
from .utils.contextGenerators import genMainContext
from .utils.queryFormatters import topLikes

# Create your views here.

def HOME(request):
    receitasQueried = topLikes(Receita.objects.all())[:12] #TODO: adicionar filtro por número de likes
    contextGenerated = genMainContext(1)
    contextGenerated.update({"isHome": True})

    return render(request, "pages/menu.html",
                  context={
                      "pageDetails": contextGenerated,
                      "receitas": receitasQueried
                    },
                  content_type="text/html")


def RECEITA(request, idRequest):
    receitaQueried = Receita.objects.get(idPage=idRequest)

    return render(
        request, "pages/receita.html/",
        context={
            "pageDetails": genMainContext(3),
            "receita": receitaQueried,
        },
        content_type="text/html")


#! faltando reorganizar templates para as seguintes Views:
#TODO: Fazer css específico de users & coleções -- consultar diagrama
def CATEGORIA(request, idRequest): #* Para selecionar categorias por cards de cada uma.
    receitasQueried = Receita.objects.filter(category__categoryType=idRequest) # double _ para 'objeto.attr'

    return render(
        request, "pages/menu.html",
        context={
            "pageDetails": genMainContext(2),
            "receitas": receitasQueried
        },
        content_type="text/html"
    )

def COLECAO_LISTING(request): #* Para mostrar coleções de receitas (Menu de coleções -> Menu com query definida de receitas)
    receitasQueried = topLikes(Receita.objects.all())[:18] #TODO: mostrar as com mais likes em suas receitas

    return render(
        request, "pages/menu.html",
        context={
            "pageDetails": genMainContext(1),
            "receitas": receitasQueried
        },
        content_type="text/html"
    )

def COLECAO(request, idRequest): #* Para selecionar categorias por cards de cada uma.
    receitasQueried = Receita.objects.filter(categoria=idRequest)

    return render(
        request, "pages/menu.html",
        context={
            "pageDetails": genMainContext(1),
            "receitas": receitasQueried
        },
        content_type="text/html"
    )

## USER
## USER_LISTING #por likes totais \


def randomRECEITA(request):  #TODO: Colocar em botão 'Me mostre uma nova!'
    maxReceitas = len(Receita.objects.all())
    randomID = randint(0, maxReceitas)

    return (
        RECEITA(request, 
                randomID)
    )
