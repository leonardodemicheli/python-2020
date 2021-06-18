from unittest import TestCase
from rechteck import Rechteck



class TestRechteck(TestCase):
    r = Rechteck(5, 3)
    def test_umfang(self):
        self.assertEqual(16, self.r.umfang())

    def test_flaeche(self):
        self.assertEqual(15, self.r.flaeche())
