from django.test import TestCase
from django.urls import reverse

class TestTemplateContent(TestCase):
    fixtures = ['projetos/fixtures/old_test_data.json']

    def test_shallGenerateMainHeaderInHome(self) -> None:
        url = reverse('Home')

        siteContent = self.client.get(url).content

        self.assertInHTML( '<h1>Em Alta</h1>', siteContent.decode('utf-8') )

    def test_shallGenerateMainHeaderInReceita_1(self) -> None:
        url = reverse('Receita', args=[0])

        siteContent = self.client.get(url).content

        self.assertInHTML( '<h4 class="receitas-details-title"> Tapioca com Frango </h4>', siteContent.decode('utf-8') )

    def test_shallGenerateMainHeaderInReceita_2(self) -> None:
        url = reverse('Receita', args=[2])

        siteContent = self.client.get(url).content

        self.assertInHTML( '<h4 class="receitas-details-title"> Strogonoff com Frango e Champignon </h4>', siteContent.decode('utf-8') )

    def test_shallGenerateMainHeaderInCategoria_1(self) -> None:
        url = reverse('Categoria', args=[1])

        siteContent = self.client.get(url).content

        self.assertInHTML( '<h1>Categoria: Café da manhã </h1>', siteContent.decode('utf-8') )
    
    def test_shallGenerateMainHeaderInCategoria_4(self) -> None:
        url = reverse('Categoria', args=[4])

        siteContent = self.client.get(url).content

        self.assertInHTML( '<h1>Categoria: Jantar </h1>', siteContent.decode('utf-8') )

#Titles na response estão estranhos porcausa do SSR?
class TestTemplateTitles(TestCase):
    fixtures = ['projetos/fixtures/old_test_data.json']

    def test_shallGenerateMainHeaderInHome(self) -> None:
        url = reverse('Home')

        siteContent = self.client.get(url).content

        self.assertInHTML( """<title>
    Home 
     
     
 - Receitas</title>""", siteContent.decode('utf-8') )

    def test_shallGenerateMainHeaderInReceita_1(self) -> None:
        url = reverse('Receita', args=[0])

        siteContent = self.client.get(url).content

        self.assertInHTML( '<title>Tapioca com Frango - Receitas</title>', siteContent.decode('utf-8') )

    def test_shallGenerateMainHeaderInReceita_2(self) -> None:
        url = reverse('Receita', args=[2])

        siteContent = self.client.get(url).content

        self.assertInHTML( '<title>Strogonoff com Frango e Champignon - Receitas</title>', siteContent.decode('utf-8') )

    def test_shallGenerateMainHeaderInCategoria_1(self) -> None:
        url = reverse('Categoria', args=[1])

        siteContent = self.client.get(url).content

        self.assertInHTML( """<title>
     
     Café da manhã  
     
 - Receitas</title>""", siteContent.decode('utf-8') )
    
    def test_shallGenerateMainHeaderInCategoria_4(self) -> None:
        url = reverse('Categoria', args=[4])

        siteContent = self.client.get(url).content

        self.assertInHTML( """<title>
     
     Jantar  
     
 - Receitas</title>""", siteContent.decode('utf-8') )