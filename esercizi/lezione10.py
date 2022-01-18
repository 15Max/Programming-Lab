from lezione9 import FitIncrementModel
from lezione8 import IncrementModel
from lezione6 import NumericalCSVFile



def evaluate_fit_increment_model(fit_dataset , evaluation_test):
    # Creo una lista per contenere i vari errori
    error = []
    #Creo una lista che conterrà i valori predetti dal modello
    predictions = []

    full_dataset = fit_dataset + evaluation_test
    fit_increment_model = FitIncrementModel()
    
    







    return sum(error) / len(error)

def predict(data):
    


     
    

def evaluate_increment_model(fit_dataset , evaluation_test):
    error = []
    predictions = []



    return sum(error) / len(error)




file_dati = NumericalCSVFile('shampoo_sales.txt')
first_half = file_dati.getdata(0,24)
second_half = file_dati.getdata(24,)
#print("{}".format(evaluate_fit_increment_model(first_half,second_half)))
#print("{}".format(evaluate_increment_model(first_half,second_half)))




