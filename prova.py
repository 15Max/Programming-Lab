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
prova = CSVFile('data.csv')
print('{}'.format(prova.get_data()))