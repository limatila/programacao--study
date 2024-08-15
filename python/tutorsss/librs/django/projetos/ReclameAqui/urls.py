from ReclameAqui import views
from django.urls import path

urlpatterns = [  # * all available URLs. Apply 'path(url, view, other args)'
    path('', views.root_view, name="Root site"),
    path('home/', views.home, name="Início"),
    path('home/contato/', views.contato, name="Página de contatos")
]
