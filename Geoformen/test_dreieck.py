from unittest import TestCase
from dreieck import Dreieck

class TestDreieck(TestCase):
    d = Dreieck(2, 3, 4, 30, 90)
    def test_umfang(self):
        self.assertEqual(9, self.d.umfang())
