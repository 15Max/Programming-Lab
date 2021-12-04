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
        csv_file = CSVFile('shampoo_sales.txt')
        with self.assertRaises(Exception):
            csv_file.get_data(-1,4)
        
    
    def test_stings_in_arg(self):
        csv_file = CSVFile('shampoo_sales.txt')
        with self.assertRaises(Exception):
            csv_file.get_data('due',4)

    def test_list_in_arg(self):
        csv_file = CSVFile('shampoo_sales.txt')
        with self.assertRaises(Exception):
            csv_file.get_data(['due'],4)
    
    def test_dict_in_arg(self):
        csv_file = CSVFile('shampoo_sales.txt')
        with self.assertRaises(Exception):
            csv_file.get_data({1:'hi'},4)

    def test_file_length(self):
        with self.assertRaises(Exception):
            csv_file = CSVFile('shampoo_sales.txt')
            csv_file.get_data(1, 100)
    
    def test_file_name_type(self):
        with self.assertRaises(Exception):
            csv_file = CSVFile(2)
            
    def test_file_name_type_2(self):
        with self.assertRaises(Exception):
            csv_file = CSVFile(['shampoo_sales.txt'])
    
    def test_file_name_type_3(self):
        with self.assertRaises(Exception):
            csv_file = CSVFile({1:'shampoo_sales.txt'})
    
