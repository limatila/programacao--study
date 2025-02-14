from django.test import TestCase
from Receitas.models import Receita, Category, Step
from django.contrib.auth.models import User
from django.core.management import call_command

class ReceitaSaveTest(TestCase):

    def test_defaultSaveShallCreateCorrectReceita(self):
        #Arrange
        self.titleReceitaInserted = 'Receita de Teste'
        self.imageReceitaInserted = 'receita-covers/default.jpg' # fugindo da restri o de imagem obrigat ria
        self.descriptionResumedInserted = 'Receita de Teste'
        self.descriptionInserted = 'Receita de Teste'
        self.preparationTimeInserted = 10
        self.preparationTimeUnitInserted = 'minutos'
        self.categoryInserted = Category.objects.create(categoryType='1')
        self.userSubmittedInserted = User.objects.create_user(username='test', password="123", email='test@mail.com')
        self.likesInserted = 10

        #Act
        receitaSaved = Receita.objects.create(
                titleReceita=self.titleReceitaInserted,
                imageReceita=self.imageReceitaInserted,
                descriptionResumed=self.descriptionResumedInserted,
                description=self.descriptionInserted,
                preparationTime=self.preparationTimeInserted,
                preparationTimeUnit=self.preparationTimeUnitInserted,
                category=self.categoryInserted,
                userSubmitted=self.userSubmittedInserted,
                likes=self.likesInserted
        )

        #Assert
        self.assertEqual(receitaSaved.titleReceita, self.titleReceitaInserted)
        self.assertEqual(receitaSaved.imageReceita, self.imageReceitaInserted)
        self.assertEqual(receitaSaved.descriptionResumed, self.descriptionResumedInserted)
        self.assertEqual(receitaSaved.description, self.descriptionInserted)
        self.assertEqual(receitaSaved.preparationTime, self.preparationTimeInserted)
        self.assertEqual(receitaSaved.preparationTimeUnit, self.preparationTimeUnitInserted)
        self.assertEqual(receitaSaved.category.categoryType, self.categoryInserted.categoryType)
        self.assertEqual(receitaSaved.userSubmitted.username, self.userSubmittedInserted.username)
        self.assertEqual(receitaSaved.likes, self.likesInserted)

    def test_defaultSaveShallCreateCorrectCategory(self):
        #Arrange
        self.categoryTypeInserted = '101'
        self.imageCategoryInserted = 'category-covers/default.jpg'

        #Act
        categorySaved = Category.objects.create(
                categoryType=self.categoryTypeInserted,
                imageCategory=self.imageCategoryInserted
        )

        #Assert
        self.assertEqual(categorySaved.categoryType, self.categoryTypeInserted)
        self.assertEqual(categorySaved.imageCategory, self.imageCategoryInserted)
        
    def test_defaultSaveShallCreateCorrectSteps(self):
        #Carregando fixtures programaticamente
        call_command('loaddata', "projetos/fixtures/old_test_data.json", verbosity=0)
        
        #Arrange
        self.stepNumberInserted = 1
        self.stepDescriptionInserted = "Cozinha por 1 minuto"
        self.receitaInserted = Receita.objects.get(idPage=1)

        #Act
        stepSaved = Step.objects.create(
                stepNumber=self.stepNumberInserted,
                stepDescription=self.stepDescriptionInserted,
                receita=self.receitaInserted
        )
        
        #Assert
        self.assertEqual(stepSaved.stepNumber, self.stepNumberInserted)
        self.assertEqual(stepSaved.stepDescription, self.stepDescriptionInserted)
        self.assertEqual(stepSaved.receita, self.receitaInserted)
        self.assertEqual(stepSaved.receita.titleReceita, self.receitaInserted.titleReceita)
