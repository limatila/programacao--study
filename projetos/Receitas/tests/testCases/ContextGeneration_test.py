from django.test import TestCase
from django.core.management import call_command
from django.urls import reverse

from Receitas.utils import contextGenerators
from testUtils.contextFormatters import filterDefaultContextKeys

#Generators padrões
class TestContextGenerationFunctions(TestCase):
    #Carregando dados de teste
    fixtures: list[str] = ["projetos/Receitas/tests/fixtures/dump_receita_1.json"]
    
    def test_shallGenerateCorrectContextForHome(self) -> None:
        detailsAttr = "pageDetails"
        contextExpected = contextGenerators.genMainContext(1)
        
        urlGenerated = reverse('Home')
        contextGenerated = (
            self.client.get(urlGenerated).context.get(detailsAttr)
        )
        contextResulted = filterDefaultContextKeys(contextGenerated)

        self.assertDictEqual(contextResulted, contextExpected)

    def test_shallGenerateCorrectContextForReceita(self) -> None:
        detailsAttr = "pageDetails"
        contextExpected = contextGenerators.genMainContext(2)
        
        urlGenerated = reverse('Receita', args=[1])
        contextGenerated = (
            self.client.get(urlGenerated).context.get(detailsAttr)
        )
        contextResulted = filterDefaultContextKeys(contextGenerated)

        self.assertDictEqual(contextResulted, contextExpected)

    def test_shallGenerateCorrectContextForCategory(self) -> None:
        detailsAttr = "pageDetails"
        contextExpected = contextGenerators.genMainContext(3)
        
        urlGenerated = reverse('Categoria', args=[1])
        contextGenerated = (
            self.client.get(urlGenerated).context.get(detailsAttr)
        )
        contextResulted = filterDefaultContextKeys(contextGenerated)

        self.assertDictEqual(contextResulted, contextExpected)

        #! adicionar mais posteriormente para coleçoes e users

#Generators de status 404
class TestContextNotFoundGenerationFunctions(TestCase):
    def test_shallGenerateNotFoundContextForHome(self) -> None:
        contextExpected = contextGenerators.genNotFoundContext(1)

        urlGenerated = reverse('Home')
        contextGenerated = self.client.get(urlGenerated).context["404_message"]

        self.assertEqual(contextGenerated, contextExpected)
    
    def test_shallGenerateNotFoundContextForReceita(self) -> None:
        contextExpected = contextGenerators.genNotFoundContext(2)

        urlGenerated = reverse('Receita', args=[1]) #Não existe em Db de teste
        contextGenerated = self.client.get(urlGenerated).context["404_message"]

        self.assertEqual(contextGenerated, contextExpected)
    
    def test_shallGenerateNotFoundContextForCategory(self) -> None:
        contextExpected = contextGenerators.genNotFoundContext(3)

        urlGenerated = reverse('Categoria', args=[1])
        contextGenerated = self.client.get(urlGenerated).context["404_message"]

        self.assertEqual(contextGenerated, contextExpected)
    
        #! adicionar mais posteriormente para coleçoes e users
