from django.shortcuts import render

from tests.fakeDataTests.Receitas.fakes import main as genFakeData

# Create your views here.

def HOME(request):
    return render(request, "pages/home-receitas.html",
                  context={
                      "receitas": [ genFakeData(num) for num in range(5) ] 
                    },
                  content_type="text/html")
