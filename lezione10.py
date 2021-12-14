from lezione9 import FitIncrementModel
from lezione8 import IncrementModel
from lezione6 import NumericalCSVFile


file_dati = NumericalCSVFile('shampoo_sales.txt')
dataset = file_dati.get_data()
first = dataset[:25]
last = dataset[25:]
previsioni = []
errori
incremento = FitIncrementModel()
incremento.fit(first[:-3])
incremento.predict(first[:-3])







