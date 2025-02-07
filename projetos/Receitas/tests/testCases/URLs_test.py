from django.test import TestCase
from django.urls import reverse, resolve

class TestPageURLs(TestCase):
    def test_shallReturnCorrectRootUrl(self):
        url = reverse('Root')
        self.assertEqual(url, '/')
    
    def test_shallReturnCorrectHomeUrl(self):
        url = reverse('Home')
        self.assertEqual(url, '/home/')

    def test_shallReturnCorrectReceitaUrl(self):
        # Triple A method -- Arrange, Act, and Assert
        number_for_id = 1
        
        url = reverse('Receita', args=[number_for_id]) #path necessita do argumento 'idRequest'
       
        self.assertEqual(url, f'/receita/{number_for_id}/')
    
    def test_shallReturnCorrectCategoriaUrl(self):
        number_for_id = 6

        url = reverse('Categoria', args=[number_for_id]) #path necessita do argumento 'idRequest'
        
        self.assertEqual(url, f'/categoria/{number_for_id}/')

class TestTemplateDeliver(TestCase):
    fixtures = ['projetos/fixtures/old_test_data.json'] #Verificando template de cards

    #Root não testada: não é aplicado render, e sim outra View.

    def test_urlShallGetCorrectTemplateForHome(self) -> None:
        url = reverse('Home')

        generatedView = self.client.get(url)

        #Heads
        self.assertTemplateUsed(generatedView, 'partials/heads/default-head.html')
        self.assertTemplateUsed(generatedView, 'partials/heads/head-components/style-home.html')
        self.assertTemplateUsed(generatedView, 'partials/heads/head-components/style-cards.html')

        #Body
        self.assertTemplateUsed(generatedView, 'pages/menu.html')
        self.assertTemplateUsed(generatedView, 'partials/components/receita-card.html')

    def test_urlShallGetCorrectTemplateForReceita(self) -> None:
        number_for_id = 1
        url = reverse('Receita', args=[number_for_id])

        generatedView = self.client.get(url)

        #Heads
        self.assertTemplateUsed(generatedView, 'partials/heads/default-head.html')
        self.assertTemplateUsed(generatedView, 'partials/heads/head-components/style-cards.html')

        #Body
        self.assertTemplateUsed(generatedView, 'pages/receita.html/')
        self.assertTemplateUsed(generatedView, 'partials/components/receita-card.html')

    def test_urlShallGetCorrectTemplateForCategoria(self) -> None:
        number_for_id = 1
        url = reverse('Categoria', args=[number_for_id])

        generatedView = self.client.get(url)

        self.assertTemplateUsed(generatedView, template_name='pages/menu.html') #! Deve atualizar para 'simplemenu.html'
