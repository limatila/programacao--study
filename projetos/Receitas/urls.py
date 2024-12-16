from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.HOME, name="Home"),
    path('receita/<int:idRequest>/', views.RECEITA, name="Receita"),
    path('categoria/<int:idRequest>/', views.CATEGORIA, name="Categoria"),
]
