from django.shortcuts import render
from .models import Receita, Category

from random import randint
from tests.fakeDataTests.Receitas.fakes import main as genFakeData
from .utils.contextGenerators import genMainContext

# Create your views here.

def HOME(request):
    receitasQueried = Receita.objects.all()[:12] #TODO: adicionar filtro por número de likes

    return render(request, "pages/home-receitas.html",
                  context={
                      "pageDetails": genMainContext(1),
                      "receitas": receitasQueried
                    },
                  content_type="text/html")


def RECEITA(request, idRequest):
    receitaQueried = Receita.objects.get(idPage=idRequest)

    return render(
        request, "pages/receita.html/",
        context={
            "pageDetails": genMainContext(2),
            "receita": receitaQueried,
        },
        content_type="text/html")



#TODO: outras views de receitas
def CATEGORIA_LISTING(request): #* Para um menu de cards, com cada uma das categorias
    allCategorys = Category.objects.all()
    allNames = [category.get_categoryType_display() for category in allCategorys]

    return render(
        request, "pages/home-receitas.html",
        context={
            "pageDetails": genMainContext(1),
            "receitas": allNames
        },
        content_type="text/html")

def CATEGORIA(request, idCategoria): #* Para selecionar categorias por cards de cada uma.
    receitasQueried = Receita.objects.filter(categoria=idCategoria)

    return render(
        request, "pages/home-receitas.html",
        context={
            "pageDetails": genMainContext(3),
            "receitas": receitasQueried
        },
        content_type="text/html"
    )

def COLECAO_LISTING(request): #* Para mostrar coleções de receitas (Menu de coleções -> Menu com query definida de receitas)
    receitasQueried = Receita.objects.all()[:12] #TODO: mostrar as com mais likes em suas receitas

    return render(
        request, "pages/home-receitas.html",
        context={
            "pageDetails": genMainContext(1),
            "receitas": receitasQueried
        },
        content_type="text/html"
    )

def COLECAO(request, idColecao): #* Para selecionar categorias por cards de cada uma.
    receitasQueried = Receita.objects.filter(categoria=idColecao)

    return render(
        request, "pages/home-receitas.html",
        context={
            "pageDetails": genMainContext(1),
            "receitas": receitasQueried
        },
        content_type="text/html"
    )

## USER
## USER_LISTING #por likes totais
def randomRECEITA(request):  #TODO: Para botão 'Me mostre uma nova!'
    randomID = randint(0, 5)
    return RECEITA(request, randomID) #? Vai enviar pro url certo? provavel que não.
