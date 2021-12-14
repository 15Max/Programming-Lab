import unittest
from lezione8 import IncrementModel

class TestIncrementModel(unittest.TestCase):
    # testo che il risultato sia quello atteso in generale
    def test_increment(self):
        dati = [50 , 52 , 60]
        expectation = 65.0
        model = IncrementModel()
        self.assertEqual(model.predict(dati),expectation)

    # Testo che con dati diversi il risultato sia diverso

    