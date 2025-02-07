from django.test import TestCase
from django.core.management import call_command
from django.urls import reverse

from Receitas.utils import contextGenerators
from testUtils.contextFormatters import filterDefaultContextKeys
from testUtils.contextCheckers import checkAllFalse_NotFound

#Generators padrões
class TestContextGenerationFunctions(TestCase):
    #Carregando dados de teste -> receitas existentes
    fixtures: list[str] = ["projetos/fixtures/old_test_data.json"]
    
    def test_shallGenerateCorrectContextForHome(self) -> None:
        detailsAttr = "pageDetails"
        contextExpected = contextGenerators.genMainContext("DefaultMenu")
        
        urlGenerated = reverse('Home')
        contextGenerated = (
            self.client.get(urlGenerated).context.get(detailsAttr)
        )
        contextResulted = filterDefaultContextKeys(contextGenerated)

        self.assertDictEqual(contextResulted, contextExpected)
        self.assertEqual(contextGenerated["isDefaultMenu"], True)

    def test_shallGenerateCorrectContextForReceita(self) -> None:
        detailsAttr = "pageDetails"
        contextExpected = contextGenerators.genMainContext("ReceitaDetail")
        
        urlGenerated = reverse('Receita', args=[1])
        contextGenerated = (
            self.client.get(urlGenerated).context.get(detailsAttr)
        )
        contextResulted = filterDefaultContextKeys(contextGenerated)

        self.assertDictEqual(contextResulted, contextExpected)
        self.assertEqual(contextGenerated["isReceitaDetail"], True)

    def test_shallGenerateCorrectContextForCategory(self) -> None:
        detailsAttr = "pageDetails"
        contextExpected = contextGenerators.genMainContext("SimpleMenu")
        
        urlGenerated = reverse('Categoria', args=[1])
        contextGenerated = (
            self.client.get(urlGenerated).context.get(detailsAttr)
        )
        contextResulted = filterDefaultContextKeys(contextGenerated)

        self.assertDictEqual(contextResulted, contextExpected)
        self.assertEqual(contextGenerated["isSimpleMenu"], True)
        #! adicionar mais posteriormente para coleçoes e users

#Generators de status 404
class TestContextNotFoundGenerationFunctions(TestCase):
    def test_shallGenerateNotFoundContextForHome(self) -> None:
        contextExpected = contextGenerators.genNotFoundContext("DefaultMenu")

        urlGenerated = reverse('Home')
        contextGenerated = self.client.get(urlGenerated).context

        self.assertEqual(contextGenerated["404_message"], contextExpected)
        self.assertTrue(
            checkAllFalse_NotFound(contextGenerated["pageDetails"])
        )
        
    
    def test_shallGenerateNotFoundContextForReceita(self) -> None:
        contextExpected = contextGenerators.genNotFoundContext("ReceitaDetail")

        urlGenerated = reverse('Receita', args=[1]) #Não existe em Db de teste
        contextGenerated = self.client.get(urlGenerated).context

        self.assertEqual(contextGenerated["404_message"], contextExpected)
        self.assertTrue(
            checkAllFalse_NotFound(contextGenerated["pageDetails"])
        )
    
    def test_shallGenerateNotFoundContextForCategory(self) -> None:
        contextExpected = contextGenerators.genNotFoundContext("SimpleMenu")

        urlGenerated = reverse('Categoria', args=[1])
        contextGenerated = self.client.get(urlGenerated).context

        self.assertEqual(contextGenerated["404_message"], contextExpected)
        self.assertTrue(
            checkAllFalse_NotFound(contextGenerated["pageDetails"])
        )

        #! adicionar mais posteriormente para coleçoes e users
