from unittest import TestCase
from kreis import Kreis

class TestKreis(TestCase):
    k = Kreis(1)
    def test_umfang(self):
        self.assertEqual(6.2831852, self.k.umfang())

    def test_flaeche(self):
        self.assertEqual(3.1415926, self.k.flaeche())
