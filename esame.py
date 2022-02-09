#Creo una classe per le eccezioni
class ExamException(Exception):
    pass
#Importo datetime
from datetime import datetime

#Creo la classe CSVTimeSeriesFile
class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name
        
    #Definisco il metodo get_data richiesto
    def get_data(self):

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
      

        # Lista che conterrà i valori da ritornare
        data = []

        # Leggo le righe del file e via via aggiungo gli elementi
        for line in my_file:
            #Se la riga che prendo in considerazione è una stringa procedo con delle operazioni di controllo su di essa
            if  isinstance(line,str):
                #Procedo dividendo gli elementi separati da virgola
                elements = line.split(',')

                #Controllo che ci siano almeno due elementi nella riga
                a = len(elements) > 1

                #Tolgo eventuali spazi in eccesso dai miei dati
                dates = element[0].strip()
                passenger_values = element[1].strip()
                
                #Controllo di avere come primo elemento una data del tipo aaaa-mm 
                if len(check) == 2 and check[0].isdigit() and check[1].isdigit() :
                    check[0] = int(check[0])
                    check[1] = int(check[1])
                    #Controllo che i valori delle stringhe siano accettabili
                    anno = check[0]>= 1000 and check[0]<=2022
                    mese = check[1] > 0 and check[1] <= 12
                    b = anno and mese
                else:
                    b = False

                #Controllo che il secondo dato sia convertibile ad intero 
                c = passenger_values.isdigit()
                #Se tutte le condizioni per il dato sono verificate lo aggiungo alla lista, convertendo prima ad intero il valore realtivo al numero di passeggeri
                if a and b and c :
                    passenger_values = int(passenger_values)
                    #Se ci fossero altri dati aggiuntivi nella lista li escludo considerando soltanto i primi due elementi della lista 
                    data.append(elements[:2])
        #chiudo il file
        my_file.close()

        return data

                







            



        


