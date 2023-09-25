import unittest
from proyecto import calculate

class UnitTests(unittest.TestCase):
    def test_calculate(self):
        actual = calculate([2,6,2,8,4,0,1,5,7])
        expected = {
            'Media': 3.888888888888889,
            'Varianza': 6.987654320987654,
            'Desviación Estándar': 2.6434171674156266,
            'Máximo': 8,
            'Mínimo': 0,
            'Suma de Filas': [11, 15, 9],
            'Suma de Columnas': [10, 12, 13],
            'Suma de Elementos': 35
        }
        self.assertAlmostEqual(actual, expected, "Expected different output when calling 'calculate()' with '[2,6,2,8,4,0,1,5,7]'")

    def test_calculate2(self):
        actual = calculate([9,1,5,3,3,3,2,9,0])
        expected = {
            'Media': 3.888888888888889,
            'Varianza': 9.209876543209875,
            'Desviación Estándar': 3.0347778408328137,
            'Máximo': 9,
            'Mínimo': 0,
            'Suma de Filas': [14, 13, 8],
            'Suma de Columnas': [15, 9, 11],
            'Suma de Elementos': 35
        }
        self.assertAlmostEqual(actual, expected, "Expected different output when calling 'calculate()' with '[9,1,5,3,3,3,2,9,0]'")
    
    def test_calculate_with_few_digits(self):
        self.assertRaisesRegex(ValueError, "List must contain nine numbers.", calculate, [2,6,2,8,4,0,1,])

if __name__ == "__main__":
    unittest.main()
