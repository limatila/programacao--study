from django.shortcuts import render

from tests.fakeDataTests.Receitas.fakes import main as genFakeData

# Create your views here.

def HOME(request):
    return render(request, "pages/home-receitas.html",
                  context={
                      "pageDetails": {"isHome": True},
                      "receitas": [ genFakeData(num) for num in range(5) ],
                    },
                  content_type="text/html")

def RECEITA(request, idReceita):
    return render(request, "pages/receita.html/{{ idReceita }}",
                  context={
                      "receita": genFakeData(idReceita),
                      "pageDetails": {"isReceita": True,
                                      "isHome": False},
                    },
                  content_type="text/html")