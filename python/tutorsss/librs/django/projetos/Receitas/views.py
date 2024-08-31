from django.shortcuts import render

# Create your views here.

def HOME(request):
    return render(request, "home-receitas.html",
                  context={},
                  content_type="text/html",)
