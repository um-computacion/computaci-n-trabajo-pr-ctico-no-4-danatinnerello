from src.factorial import factorial_NO_recursiva

import unittest

class Test_factorial(unittest.TestCase):
    def test_with_simple_case1(self):
        n=0
        result = factorial_NO_recursiva(n)
        self.assertEqual(result,1)

    def test_with_simple_case2(self):
        n=1
        result = factorial_NO_recursiva(n)
        self.assertEqual(result,1)

    def test_with_simple_case3(self):
        n=2
        result = factorial_NO_recursiva(n)
        self.assertEqual(result,2)

    def test_with_simple_case4(self):
        n=3
        result = factorial_NO_recursiva(n)
        self.assertEqual(result,6)

    def test_with_simple_case5(self):
        n=4
        result = factorial_NO_recursiva(n)
        self.assertEqual(result,24)
    
    def test_with_simple_case6(self):
        n=5
        result = factorial_NO_recursiva(n)
        self.assertEqual(result,120)

    def test_with_simple_case7(self):
        n=6
        result =factorial_NO_recursiva(n)
        self.assertEqual(result,720)

    def test_with_simple_case8(self):
        n=7
        result = factorial_NO_recursiva(n)
        self.assertEqual(result,5040)

    def test_with_simple_case9(self):
        n=8
        result = factorial_NO_recursiva(n)
        self.assertEqual(result,40320)

    def test_with_simple_case10(self):
        n=9
        result = factorial_NO_recursiva(n)
        self.assertEqual(result,362880)




if __name__ == "__main__":
    unittest.main()