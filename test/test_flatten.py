import unittest
from src.flatten import aplanar_lista
from src.flatten import SoloListasError

class TestAplanarLista(unittest.TestCase):
    def test_lista_simple(self):
        entrada = [1, 2, [3, 4]]
        salida_esperada = [1, 2, 3, 4]
        self.assertEqual(aplanar_lista(entrada), salida_esperada)

    
    def test_lista_anidada(self):
        entrada = [1, [2, [3, 4]], 5]
        salida_esperada = [1, 2, 3, 4, 5]
        self.assertEqual(aplanar_lista(entrada), salida_esperada)

    def test_error_por_tupla(self):
        # Verificamos que lance la excepción si hay una tupla
        entrada = [1, (2, 3)]
        with self.assertRaises(SoloListasError):
            aplanar_lista(entrada)

    def test_error_por_dict(self):
        # Verificamos que lance la excepción si hay un diccionario
        entrada = [1, {"a": 1}]
        with self.assertRaises(SoloListasError):
            aplanar_lista(entrada)

if __name__ == "__main__":
    unittest.main()