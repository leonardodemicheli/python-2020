from unittest import TestCase
from quadrat import Quadrat



class Testquadrat(TestCase):
    q = Quadrat(5)
    def test_umfang(self):
        self.assertEqual(20, self.q.umfang())

    def test_flaeche(self):
        self.assertEqual(25, self.q.flaeche())
