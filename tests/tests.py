import unittest
from src.operations import addition, subtraction, multiplication, division, square, root, factorial

class TestAddition(unittest.TestCase):
    def test_addition_integers(self):
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(-1, -1), -2)
        self.assertEqual(addition(0, 0), 0)

    def test_addition_float(self):
        self.assertEqual(addition(2.5, 2.1), 4.6)
        self.assertEqual(addition(-1.5, -1.5), -3)
        self.assertEqual(addition(0.5, 0.5), 1)

    def test_addition_mixed(self):
        self.assertEqual(addition(2.5, 1), 3.5)
        self.assertEqual(addition(2, 1.8), 3.8)

class TestSubtraction(unittest.TestCase):
    def test_subtraction_integers(self):
        self.assertEqual(subtraction(2, 3), -1)
        self.assertEqual(subtraction(-1, -1), 0)
        self.assertEqual(subtraction(0, 0), 0)

    def test_subtraction_float(self):
        self.assertEqual(subtraction(2.5, 3), -0.5)
        self.assertEqual(subtraction(2.5, 1.3), 1.2)
        self.assertEqual(subtraction(-2.5, -2.5), 0)

    def test_subtraction_mixed(self):
        self.assertEqual(subtraction(2.5, 1), 1.5)
        self.assertEqual(subtraction(-5, 3.5), -8.5)

class TestMultiplication(unittest.TestCase):
    def test_multiplication_integers(self):
        self.assertEqual(multiplication(5, 5), 25)
        self.assertEqual(multiplication(-1, -1), 1)
        self.assertEqual(multiplication(8, 8), 64)
        self.assertEqual(multiplication(0, 4), 0)

    def test_multiplication_float(self):
        self.assertEqual(multiplication(2.5, 2), 5)
        self.assertEqual(multiplication(1, 2.5), 2.5)

    def test_multiplication_mixed(self):
        self.assertEqual(multiplication(2.5, 1), 2.5)
        self.assertEqual(multiplication(-1.5, -1), 1.5)


class TestDivision(unittest.TestCase):

    def test_division_integers(self):
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(9, 3), 3)
        self.assertEqual(division(-6, -3), 2)

    def test_division_floats(self):
        self.assertEqual(division(10.0, 2.0), 5.0)
        self.assertEqual(division(9.5, 2.0), 4.75)

    def test_division_mixed(self):
        self.assertEqual(division(10, 2.5), 4.0)
        self.assertEqual(division(7.5, 2), 3.75)

    def test_division_by_zero(self):
        self.assertEqual(division(10, 0), "Error: Division by zero")
        self.assertEqual(division(-5, 0), "Error: Division by zero")
        self.assertEqual(division(0, 0), "Error: Division by zero")


class TestSup(unittest.TestCase):

    def test_square(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(-3), 9)
        self.assertEqual(square(0), 0)
        self.assertEqual(square(10), 100)

    def test_root(self):
        self.assertEqual(root(4), 2)
        self.assertEqual(root(9), 3)
        self.assertAlmostEqual(root(2), 1.4142135623730951)
        self.assertEqual(root(0), 0)

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(7), 5040)

if __name__ == '__main__':
    unittest.main()