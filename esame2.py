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

        #Lista contentente i valori da ritornare
        data = []

        # leggo le righe del file
        for line in my_file:
            #lista contenente gli elementi della riga splittati
            elements = line.split(',')
            #Tolgo l'elemento new line (/n)
            elements[-1] = elements[-1].strip()
            #Se non sto leggendo l'intestazione
            if elements[0] != 'date':
                #Se la riga ha un solo dato la salto
                if len(elements) < 2 :
                    continue
                #Tolgo eventuali spazi in eccesso 
                elements[0] = elements[0].strip()
                elements[1] = elements[1].strip()

                #Controllo che il primo dato sia convertibile in oggetto datetime
                try:
                    prova_1 = datetime.strptime(elements[0], '%Y-%m')
                except:
                    continue
                
                #Controllo che il secondo dato sia tramutabile in intero e lo converto
                try:
                    elements[1] = int(elements[1])
                except:
                    # Se non riesco a convertire il dato in intero lo sostituisco con None
                    elements[1] = None
                # Se hanno superato tutti i controlli aggiungo i due elementi alla lista, con lo slicing escludo eventuali elementi in eccesso
                data.append(elements[:2])





                


                
        #Chiudo il file        
        my_file.close()
        return data
     
prova = CSVFile('data.csv')
print('{}'.format(prova.get_data()))