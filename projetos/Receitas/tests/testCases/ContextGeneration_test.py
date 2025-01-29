from django.test import TestCase
from django.urls import reverse, resolve

from Receitas.models import Receita, Category
from Receitas.utils import contextGenerators

#Generators padrões
class TestContextGenerationFunctions(TestCase):
    ##! Certificar uso do DB de produção
    def test_shallGenerateCorrectContextForHome(self) -> None:
        contextExpected = contextGenerators.genMainContext(1)
        
        urlGenerated = reverse('Home')
        contextGenerated = self.client.get(urlGenerated).context

        self.assertDictEqual(contextGenerated, contextExpected)

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
        contextExpected = contextGenerators.genNotFoundContext(1)

        urlGenerated = reverse('Categoria', args=[1])
        contextGenerated = self.client.get(urlGenerated).context["404_message"]

        self.assertEqual(contextGenerated, contextExpected)
    
    #! adicionar mais posteriormente para coleçoes e users
