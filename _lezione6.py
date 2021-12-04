import unittest
from lezione6 import CSVFile

class TestGetData(unittest.TestCase):
    
    def test_file_name_type(self):
        with self.assertRaises(Exception):
            csv_file = CSVFile(2)