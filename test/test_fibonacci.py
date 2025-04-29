import unittest
from src.fibonacci import fibonacci_NO_recursiva


class testFibonacci(unittest.TestCase):
    def test_1(self):
        n = 0 

        result = fibonacci_NO_recursiva(n)

        self.assertEqual(result, 0)

    def test_2(self):
        n = 1
        result = fibonacci_NO_recursiva(n)
        self.assertEqual(result, 1)

    def test_3(self):
        n = 2
        result = fibonacci_NO_recursiva(n)
        self.assertEqual(result, 1)

    def test_4(self):
        n = 7
        result = fibonacci_NO_recursiva(n)
        self.assertEqual(result, 13)

    def test_5(self):
        n = 5
        result = fibonacci_NO_recursiva(n)
        self.assertEqual(result, 5)

    def test_6(self):
        n = 10
        result = fibonacci_NO_recursiva(n)
        self.assertEqual(result, 88)

if __name__ == "__main__":
    unittest.main()