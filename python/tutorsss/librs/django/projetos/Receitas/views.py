from django.shortcuts import render

from tests.fakeDataTests.Receitas.fakes import main as genFakeData

# Create your views here.

def HOME(request):
    return render(request, "pages/home-receitas.html",
                  context={
                      "title": "Home",
                      "pageDetails": {"isHome": True},
                      "receitas": [ genFakeData(num) for num in range(5) ],
                    },
                  content_type="text/html")

def RECEITA(request, idReceita):
    return render(request, "pages/receita.html/",
                  context={
                      "title": f"Receita id{idReceita}",
                      "receita": genFakeData(idReceita), #TODO: Ao implementar BD, idReceita deve ser usado para consultar ela.
                      "pageDetails": {"isReceita": True,
                                      "isHome": False},
                    },
                  content_type="text/html")