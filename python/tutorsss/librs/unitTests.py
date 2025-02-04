# Run with: "python -m unittest <filename>"
# Can use "python -m unittest discover" with '-s <test_directory>', and '-p <pattern>' to search for files in set pattern (like '*_test.py' or 'test_*.py')
# Ideally you wanna create a pytest.ini file to set usefull configurations.

from unittest import TestCase #Default, not the ideal for use as it's logs aren't good for reading

#Define a main class to run the tests
class TestStringMethods(TestCase): #will inherit from default TestCase, for usage of custom (better) assertions
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO') #Confirms that values inserted are equal: #*pattern (Result, Expected)

    def test_isupper(self):
        #* Boolean checking
        self.assertTrue('FOO'.isupper()) 
        self.assertFalse('Foo'.isupper())

    def test_equations(self):
        #* Math operations inserted inside argument
        self.assertEqual(1 + 1, 2)
        self.assertEqual(2 * 2, 4)
        self.assertEqual(3 ** 3, 27)

    def test_comparatives(self):
        #* Comparing values...
        number_one = 1
        number_two = 2

        self.assertLess(number_one, number_two)
        self.assertGreater(number_two, number_one)
        self.assertEqual(number_one, number_one)
        
        self.assertFalse(number_one == number_two)
        self.assertTrue(number_one <= (number_two + 50))
        #And there's more to discover

    def test_tripleA_method(self):
        #* A common method for modern and secure testing, handling small size operations each time.
        # Arrange - Assume this is a program to stract a name from the String
        input: str = "Meu nome é Átila"
        expected: str = "Átila"

        # Act
        indexFound = input.find("Átila")
        result: str = input[ indexFound : indexFound+5 ]

        # Assert
        self.assertEqual(expected, result)