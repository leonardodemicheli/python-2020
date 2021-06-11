from unittest import TestCase
from calculator import Calculator


class TestCalculator(TestCase):
    a = Calculator(3, 2)

    def test_add(self):
        self.assertEqual(5, self.a.add())

    def test_sub(self):
        self.assertEqual(1, self.a.sub())

    def test_mul(self):
        self.assertEqual(6, self.a.mul())

    def test_div(self):
        self.assertEqual(1.5, self.a.div())

    def test_mod(self):
        self.assertEqual(1, self.a.mod())
