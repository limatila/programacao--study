from django.http import Http404
from django.shortcuts import render

from .models import Receita
#test: from tests.fakeDataTests.Receitas.fakes import main as genFakeData

from random import randint
from .utils.contextGenerators import *
from .utils.queryFormatters import topLikes

# View padrão code 404
def NOT_FOUND(request, pageNumberForGen: int):
    return render(request, "404.html", status=404,
    context={"pageDetails": genMainContext(pageNumberForGen),
             "404_message": genNotFoundContext(pageNumberForGen)} )

# Create your views here.


def HOME(request):
    CONTEXT_CHOICE = "DefaultMenu"
    receitasQueried = topLikes(
        Receita.objects.all())[:
                               12]  #TODO: adicionar filtro por número de likes

    if not receitasQueried:
        return NOT_FOUND(request, CONTEXT_CHOICE)
    else:
        contextGenerated = genMainContext(CONTEXT_CHOICE)
        contextGenerated.update({"isHome": True})

    return render(request,
                  "pages/menu.html",
                  context={
                      "pageDetails": contextGenerated,
                      "receitas": receitasQueried
                  },
                  content_type="text/html")


def RECEITA(request, idRequest: int):
    CONTEXT_CHOICE = "ReceitaDetail"
    try:
        receitaQueried = Receita.objects.get(idPage=idRequest)
    except Receita.DoesNotExist:
        return NOT_FOUND(request, CONTEXT_CHOICE)

    return render(request,
                  "pages/receita.html/",
                  context={
                      "pageDetails": genMainContext(CONTEXT_CHOICE),
                      "receita": receitaQueried,
                  },
                  content_type="text/html")


#! faltando reorganizar templates para as seguintes Views:
#TODO: Fazer css específico de users & coleções -- consultar diagrama
def CATEGORIA(request, idRequest): #* Para selecionar categorias por cards de cada uma.
    CONTEXT_CHOICE = "SimpleMenu"
    receitasQueried = Receita.objects.filter(category__categoryType=idRequest) # double _ para 'objeto.attr'

    if not receitasQueried:
        return NOT_FOUND(request, CONTEXT_CHOICE)

    return render(
        request, "pages/menu.html",
        context={
            "pageDetails": genMainContext(CONTEXT_CHOICE),
            "receitas": receitasQueried
        },
        content_type="text/html"
    )

def COLECAO_LISTING(request): #* Para mostrar coleções de receitas (Menu de coleções -> Menu com query definida de receitas)
    #! Todo: verificar como vão ficar os templates para decidir qual é o contexto
    CONTEXT_CHOICE = None
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

    return (RECEITA(request, randomID))
