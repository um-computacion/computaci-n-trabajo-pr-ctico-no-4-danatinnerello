from src.factorial import factorial_recursiva
from unittest.mock import patch
import unittest

class Test_factorial(unittest.TestCase):
    def test_with_simple_case1(self):
        n=0
        result = factorial_recursiva(n)
        self.assertEqual(result,1)

    def test_with_simple_case2(self):
        n=1
        result = factorial_recursiva(n)
        self.assertEqual(result,1)

    def test_with_simple_case3(self):
        n=2
        result = factorial_recursiva(n)
        self.assertEqual(result,2)

    def test_with_simple_case4(self):
        n=3
        result = factorial_recursiva(n)
        self.assertEqual(result,6)

    def test_with_simple_case5(self):
        n=4
        result = factorial_recursiva(n)
        self.assertEqual(result,24)
    
    def test_with_simple_case6(self):
        n=5
        result = factorial_recursiva(n)
        self.assertEqual(result,120)

    def test_with_simple_case7(self):
        n=6
        result =factorial_recursiva(n)
        self.assertEqual(result,720)

    def test_with_simple_case8(self):
        n=7
        result = factorial_recursiva(n)
        self.assertEqual(result,5040)

    def test_with_simple_case9(self):
        n=8
        result = factorial_recursiva(n)
        self.assertEqual(result,40320)

    def test_with_simple_case10(self):
        n=9
        result = factorial_recursiva(n)
        self.assertEqual(result,362880)


class TestFactorial(unittest.TestCase):
    
    def test_factorial_numeros_positivos(self):
        """Prueba el cálculo de factorial para números positivos."""
        self.assertEqual(factorial_recursiva(1), 1)
        self.assertEqual(factorial_recursiva(5), 120)
        self.assertEqual(factorial_recursiva(10), 3628800)
        self.assertEqual(factorial_recursiva(20), 2432902008176640000)
    
    def test_factorial_cero(self):
        """Prueba el cálculo de factorial para cero."""
        self.assertEqual(factorial_recursiva(0), 1)
    
    def test_factorial_negativos(self):
        """Prueba que se maneje correctamente números negativos."""
        self.assertEqual(factorial_recursiva(-1), "Error: No se puede calcular el factorial de un número negativo")
        self.assertEqual(factorial_recursiva(-100), "Error: No se puede calcular el factorial de un número negativo")
    
    def test_factorial_no_numerico(self):
        """Prueba que se manejen correctamente entradas no numéricas."""
        self.assertEqual(factorial_recursiva("abc"), "Error: Por favor ingresa un número válido")
        self.assertEqual(factorial_recursiva(""), "Error: Por favor ingresa un número válido")
        self.assertEqual(factorial_recursiva("3.14"), "Error: Por favor ingresa un número válido")  # Asumiendo que solo aceptamos enteros
    
    def test_factorial_tipos_especiales(self):
        # True se convierte a 1 y False a 0 en Python al tratarlos como int
        self.assertEqual(factorial_recursiva(True), 1)
        self.assertEqual(factorial_recursiva(False), 1)



if __name__ == "__main__":
    unittest.main()