import unittest
from lezione6 import CSVFile

class TestGetData(unittest.TestCase):
    def test_get_data(self):
        csv_file = CSVFile('shampoo_sales.txt')
        Expectation = [['01-01-2012','266.0\n'],['01-02-2012','145.9\n'],['01-03-2012','183.1\n']]
        self.assertEqual(csv_file.get_data(0,3), Expectation)
    
    def test_file_name(self) :
        csv_file = CSVFile('shampoo_sales.txt')
        self.assertEqual(csv_file.name,'shampoo_sales.txt' )
    
    def test_negative(self):
        with self.assertRaises(Exception):
            
            csv_file.get_data(-1,4)
    
    def test_stings_in_arg(self):
        with self.assertRaises(TypeError):
            csv_file = CSVFile('shampoo_sales.txt')
            csv_file.get_data('due',4)
    
    def test_file_length(self):
        with self.assertRaises(Exception):
            csv_file = CSVFile('shampoo_sales.txt')
            csv_file.get_data(1, 100)
