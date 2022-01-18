import unittest
from lezione6 import NumericalCSVFile
class TestNewGetData(unittest.TestCase):
    # Test NumericalCSVFile
    def test_new_get_data(self):
        numerical_csv_file = NumericalCSVFile('shampoo_sales.txt')
        Expectation = [266.0 , 145.9 ,183.1 ]
        self.assertEqual(numerical_csv_file.get_data(0,3), Expectation)
        self.assertEqual(numerical_csv_file.get_data(None,3), Expectation)
    #Controllo che il nome del file venga effettivamente salvato come attributo self.name
    def test_file_name(self) :
        numerical_csv_file = NumericalCSVFile('shampoo_sales.txt')
        self.assertEqual(numerical_csv_file.name,'shampoo_sales.txt')