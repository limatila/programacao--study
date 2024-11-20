from . import views
from django.urls import path

urlpatterns = [
    path('', views.HOME, name="Home"),
    path('receita/<int:idReceita>/', views.RECEITA, name="Receita"),
]
