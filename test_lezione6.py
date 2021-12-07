import unittest
from lezione6 import CSVFile


class TestGetData(unittest.TestCase):

    #Controllo che se il nome del file da aprire è errato venga alzata un'eccezione
    def test_correct_file_name(self):
        with self.assertRaises(Exception):
            csv_file = CSVFile('shampo_sales.txt')
    
    # Controllo che l'output di get data  sia quello atteso
    
    def test_get_data(self):
        
        Expectation = [['01-01-2012','266.0\n'],['01-02-2012','145.9\n'],['01-03-2012','183.1\n']]
        csv_file = CSVFile('shampoo_sales.txt')
        self.assertEqual(csv_file.get_data(0,3), Expectation)
        self.assertEqual(csv_file.get_data(None,3),Expectation)
    
    #Controllo che il nome del file venga effettivamente salvato come attributo self.name
    def test_file_name(self) :
        csv_file_1 = CSVFile('shampoo_sales.txt')
        self.assertEqual(csv_file_1.name,'shampoo_sales.txt' )
    #Controllo che l'eccezione per cui uno dei due numeri in input sono negativi venga "alzata"
    def test_negative(self):
        csv_file_2 = CSVFile('shampoo_sales.txt')
        with self.assertRaises(Exception):
            csv_file_2.get_data(-1,4)
            csv_file_2.get_data(1,-4)
    #Controllo che anche dando in input un float la funzione mi restituisce il risultato atteso
    def test_get_data_1(self):
        csv_file_3 = CSVFile('shampoo_sales.txt')
        Expectation = [['01-01-2012','266.0\n'],['01-02-2012','145.9\n'],['01-03-2012','183.1\n']]
        self.assertEqual(csv_file_3.get_data(0.0,3), Expectation)
        self.assertEqual(csv_file_3.get_data(0.0,3.0), Expectation)
        self.assertEqual(csv_file_3.get_data(0,3.0), Expectation)
     #Controllo che anche dando in input una stinga numerica la funzione mi restituisce il risultato atteso
    def test_get_data_2(self):
        csv_file_4 = CSVFile('shampoo_sales.txt')
        Expectation = [['01-01-2012','266.0\n'],['01-02-2012','145.9\n'],['01-03-2012','183.1\n']]
        self.assertEqual(csv_file_4.get_data('0',3), Expectation)
        self.assertEqual(csv_file_4.get_data(0,'3'), Expectation)
        self.assertEqual(csv_file_4.get_data('0','3'), Expectation)
    #Controllo che anche dando in input una stringa float la funzione mi restuisca l'output atteso
    def test_get_data_3(self):
        csv_file = CSVFile('shampoo_sales.txt')
        Expectation = [['01-01-2012','266.0\n'],['01-02-2012','145.9\n'],['01-03-2012','183.1\n']]
        self.assertEqual(csv_file.get_data('0.0',3), Expectation)
        self.assertEqual(csv_file.get_data('0.0','3.0'), Expectation)
        self.assertEqual(csv_file.get_data(0,'3.0'), Expectation)
    def test_get_data_4(self):
        csv_file = CSVFile('shampoo_sales.txt')
        Expectation = [['01-01-2012','266.0\n'],['01-02-2012','145.9\n'],['01-03-2012','183.1\n']]
        self.assertEqual(csv_file.get_data(' 0.0 ',' 3 '), Expectation)
        self.assertEqual(csv_file.get_data(' 0.0',' 3.0'), Expectation)
        self.assertEqual(csv_file.get_data('0 ','3.0 '), Expectation)        
    #Controllo che se ho una stringa come argomento di get_data venga  alzata un'eccezione
    def test_stings_in_arg(self):
        csv_file = CSVFile('shampoo_sales.txt')
        with self.assertRaises(Exception):
            csv_file.get_data('due',4)
            csv_file.get_data(2,'quattro')
            csv_file.get_data('due','quattro')
    #Controllo che se ho una lista come argomento di get_data venga alzata un'eccezione
    def test_list_in_arg(self):
        csv_file = CSVFile('shampoo_sales.txt')
        with self.assertRaises(Exception):
            csv_file.get_data(['due'],4)
            csv_file.get_data(2,[4])
            csv_file.get_data([2],[4])
    #Controllo che se ho un dizionario come argomento di get_data venga  alzata un'eccezione
    def test_dict_in_arg(self):
        csv_file = CSVFile('shampoo_sales.txt')
        with self.assertRaises(Exception):
            csv_file.get_data({1:'hi'},4)
    #Controllo che se la lunghezza del file è minore di end venga alzata un'eccezione
    def test_file_length(self):
        with self.assertRaises(Exception):
            csv_file = CSVFile('shampoo_sales.txt')
            csv_file.get_data(1, 100)
    #Controllo che sia alzata un'eccezione se il tipo del file non è una stringa nei vari casi
    def test_file_name_type(self):
        with self.assertRaises(Exception):
            csv_file = CSVFile(2)
            csv_file = CSVFile(['shampoo_sales.txt'])
            csv_file = CSVFile({1:'shampoo_sales.txt'})


        


