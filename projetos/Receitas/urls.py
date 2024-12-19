from . import views
from django.urls import path
from django.shortcuts import redirect

#Definindo Redirecionamento da Root
def ROOT(request):
    return redirect('Home')


urlpatterns = [
    path('', ROOT, name="Root"),
    path('home/', views.HOME, name="Home"),
    path('receita/<int:idRequest>/', views.RECEITA, name="Receita"),
    path('categoria/<int:idRequest>/', views.CATEGORIA, name="Categoria"),
]
