from django.test import TestCase
from django.urls import reverse

from django.conf import settings

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