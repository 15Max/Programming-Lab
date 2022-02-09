# Importo il modulo datetime dalla libreria datetime
from datetime import datetime

#Creo una classe per le eccezioni
class ExamException(Exception):
    pass

#Creo la classe CSVFile
class CSVFile():
    def __init__(self,name):
        self.name = name
    
    def get_data(self ):

        #Controllo che il nome del file sia una stringa
        if not isinstance(self.name, str):
            raise ExamException('Il nome del file non è una stringa!')
        #Controllo che il file sia leggibile
        try:
            my_file = open(self.name, 'r')
        except Exception:
            raise ExamException("C'è stato un errore durante l'apertura del file!")
        

        #Variabile contatore 
        length = 0
        for line in my_file:
            length += 1
        #Controllo che il file non sia vuoto
        if length == 0:
            raise ExamException('Il file è vuoto!')
        
        # Initialise an empty list in which I am going to save our data.
        data = []
    
        # Lreading the file line by line
        for line in my_file:
                
            # divide each line on the comma
            elements = line.split(',')
                
            # I remove the newline element (\n) from the last element using the strip.
            elements[-1] = elements[-1].strip()
    
            # If I'm not processing the header
            if elements[0] != 'date':
                #we skip over the parts of the list which have less than 2 arguments
                if len(elements)<2:
                    continue
                #removing excess spaces
                elements[0] = elements[0].strip()
                elements[1] = elements[1].strip()

                #checking if elements[0] can be converted into datetime
                try:
                    date_time = datetime.strptime(elements[0], '%Y-%m')
                except:
                    continue

                #transform all elements from string to integer
                try:
                    elements[1] = int(elements[1])
                except:
                    elements[1] = None 
                #if i'm not able to i put none instead
  
                #I add these items to the list and in case we have more than two elements i'm gonna add just the first two 
                data.append(elements[:2])
    
        my_file.close()
        return data


#Creo la classe CSVTimeSeries

class CSVTimeSeries(CSVFile):
    def get_data(self):
        #Salvo in una variabile il risultato del get_data di CSVFile
        dati = super.get_data()


# Creo la funzione richiesta 
def compute_avg_monthly_difference(time_series, first_year, last_year):
    # Contollo che first_year e last_year siano stringhe
    if not isinstance(first_year, str) and not(last_year , str):
        raise ExamException('I dati inseriti non sono stringhe!')
    #Controllo che first_year e last_year non siano vuote
    if first_year == '' :
        raise ExamException('Il primo intervallo è una stringa vuota!')
    if last_year == '' :
        raise ExamException('Il secondo intervallo è una stringa vuota!')
    #Controllo che la striga sia un numero intero
    if not first_year.isdigit() and not last_year.isdigit():
        raise ExamException('Le stringhe non contengono numeri!')
    #Controllo che l'anno finale non sia minore di quello finale:
    if int(last_year) < int(first_year):
        raise ExamException("L'anno iniziale è maggiore dei quello finale!")
    # Controllo che l'anno iniziale sia maggiore o uguale del 1949
    if int(first_year) < 1949 :
        raise ExamException("L'intervallo di dati considerato parte dal 1949.")
    #Controllo che l'anno finale sia minore o uguale al 1960
    if int(last_year) > 1960 :
        raise ExamException("L'intervallo di dati considerato arriva fino al 1960.")

    #Controllo che il contenuto di time series sia una lista
    if not isinstance(time_series, list):
        raise ExamException('time_series non è una lista!')
    # Controllo che non sia vuota
    if time_series == [] :
        raise ExamException('La lista time_series non ha elementi!')


    #Converto in interi gli anni da considerare
    primo_anno = int(first_year)
    ultimo_anno = int(last_year)
    #Intervallo di anni da considerare
    intervallo = ultimo_anno - primo_anno
    # Lista anni
    lista_anno = []
    # Creo la lista degli anni da considerare
    for i in range(intervallo+1):
        lista_anno.append(primo_anno + i)
        



time_series_file = CSVTimeSeriesFile(name='data.csv')
#Variabile contenente il risultato di get.data()
time_series = time_series_file.get_data()
print('{}'.format(compute_avg_monthly_difference(time_series, '1949', '1951')))
