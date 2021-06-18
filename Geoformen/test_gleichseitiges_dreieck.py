from unittest import TestCase
from gleichseitiges_dreieck import Gleichseitiges_Dreick


class TestGleichseitiges_Dreick(TestCase):
    gd = Gleichseitiges_Dreick(2)
    def test_umfang(self):
        self.assertEqual(6, self.gd.umfang())
