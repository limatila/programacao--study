from django.test import TestCase #Derivado do módulo unittest

class DefaultTestTemplate(TestCase):
    def test_default_unit_test(self):
        self.assertTrue(True)
        self.assertFalse(False)  # Falsy values
        self.assertEqual(1 + 1, 2)
        self.assertIsNone(None)
        self.assertIsNotNone(False)  # Qualquer outro que None
        self.assertIsInstance("hello", str)
        self.assertIsInstance(3.14, float)
        self.assertIsInstance((1, 2, 3), tuple)

        #Comparativos
        self.assertGreater(10, 5)
        self.assertGreaterEqual(10, 10)  #e mais
        self.assertLess(5, 10)

        #Comentário em caso de erro
        self.assertFalse(False, "O desejado não aconteceu")

        #Testando print
        print("\nTeste unitário padrão executado com sucesso\n")