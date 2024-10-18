from django.shortcuts import render

from tests.fakeDataTests.Receitas.fakes import main as genFakeData

# Create your views here.

def HOME(request):
    return render(request, "pages/home-receitas.html",
                  context={
                      "title": "Home",
                      "pageDetails": {"isMainMenu": True,
                                      "isDetailMenu": False},
                      "receitas": [ genFakeData(num) for num in range(5) ], #* gera 5 fakes pra uso
                    },
                  content_type="text/html")

def RECEITA(request, idReceita):
    return render(request, "pages/receita.html/",
                  context={
                      "title": f"Receita id{idReceita}",
                      "receita": genFakeData(idReceita), #TODO: Ao implementar BD, idReceita deve ser usado para consultar ela.
                      "pageDetails": {"isMainMenu": False,
                                      "isDetailMenu": True},
                    },
                  content_type="text/html")