import unittest
from src.fibonacci import fibonacci


class testFibonacci(unittest.TestCase):
    def test_1(self):
        n = 0 

        result = fibonacci(n)

        self.assertEqual(result, 0)

    def test_2(self):
        n = 1
        result = fibonacci(n)
        self.assertEqual(result, 1)

    def test_3(self):
        n = 2
        result = fibonacci(n)
        self.assertEqual(result, 1)

    def test_4(self):
        n = 7
        result = fibonacci(n)
        self.assertEqual(result, 13)

    def test_5(self):
        n = 5
        result = fibonacci(n)
        self.assertEqual(result, 5)

    def test_6(self):
        n = 10
        result = fibonacci(n)
        self.assertEqual(result, 55)
    
    def test_fibonacci_numeros_grandes(self):
        """Prueba el cálculo de Fibonacci para números más grandes."""
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(15), 610)
        self.assertEqual(fibonacci(20), 6765)
    
    def test_fibonacci_negativos(self):
        """Prueba que se maneje correctamente números negativos."""
        self.assertEqual(fibonacci(-1), "Error: No se puede calcular Fibonacci para un número negativo")
        self.assertEqual(fibonacci(-10), "Error: No se puede calcular Fibonacci para un número negativo")
    
    def test_fibonacci_no_numerico(self):
        """Prueba que se manejen correctamente entradas no numéricas."""
        self.assertEqual(fibonacci("abc"), "Error: Por favor ingresa un número entero válido")
        self.assertEqual(fibonacci(""), "Error: Por favor ingresa un número entero válido")
        self.assertEqual(fibonacci("3.14"), "Error: Por favor ingresa un número entero válido")
    
    def test_fibonacci_tipos_especiales(self):
        # True se convierte a 1 y False a 0 en Python al tratarlos como int
        self.assertEqual(fibonacci(True), 1)
        self.assertEqual(fibonacci(False), 0)


if __name__ == "__main__":
    unittest.main()