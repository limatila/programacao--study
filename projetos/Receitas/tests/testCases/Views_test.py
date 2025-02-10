from django.test import TestCase
from django.urls import resolve, reverse

from Receitas import views
from Receitas.urls import ROOT

class TestViewAssignments(TestCase):
    #* Testes estáticos para assegurar nomes de URL e função de View
    def test_shallResolveCorrectRootView(self) -> None:
        view = resolve('/')  #Resolve a URL para a view correspondente
        
        self.assertIs(view.func, ROOT)
        print(f'Func {view.func.__name__} está designada.')

    def test_shallRedirectRootToHome(self) -> None:
        view = resolve('/')  #Resolve a URL para a view correspondente
        
        returnedUrl = view.func(request=None).url

        self.assertIs(view.func, ROOT)
        self.assertEqual( returnedUrl.strip(), reverse('Home').strip() ) #Verificando redirect
        print(f'Func {view.func.__name__} redirecionou para url {returnedUrl}')

    def test_shallResolveCorrectHomeView(self) -> None:

        view = resolve('/home/')
        
        self.assertIs(view.func, views.HOME)
        print(f'Func {view.func.__name__} está designada.') 

    #* Testes dinâmicos para nomes que podem mudar
    def test_shallResolveCorrectReceitaView(self) -> None:
        urlReversed = reverse('Receita', args=[1]) # gera a URL da Receita
        
        view = resolve(urlReversed) # gera a View com base na URL da página atribuida
        
        self.assertIs(view.func, views.RECEITA)
        print(f'Func {view.func.__name__} está designada.')
            #* Resultado: um Teste dinâmico de para a View definida em 'urls.py'

    def test_shallResolveCorrectCategoryView(self) -> None:
        urlReversed = reverse('Categoria', args=[1]) # gera a URL da Receita
        
        view = resolve(urlReversed)
        
        self.assertIs(view.func, views.CATEGORIA)
        print(f'Func {view.func.__name__} está designada.')
