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
        

        #Variabile contatore per la lunghezza del file 
        length = 0
        for line in my_file:
            length += 1
        #Controllo che il file non sia vuoto
        if length == 0:
            raise ExamException('Il file è vuoto!')

        #Apro il file

        my_file = open(self.name, 'r')

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
                    test = datetime.strptime(elements[0], '%Y-%m')
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
            
        #Controllo che le date del file siano in ordine strettamente crescente
        for i in range(len(data)-1):
            if data[i+1][0] <= data[i][0]:
                raise ExamException("Le date del file non sono nell'ordine corretto!")


        
        #Chiudo il file
        my_file.close()

        return data

#Creo la classe CSVTimeSeriesFile che erediterà dalla classe CSVFile

class CSVTimeSeriesFile(CSVFile):
    def get_data(self):
        #Salvo in una variabile il risultato del get_data di CSVFile
        dati = super().get_data()     
        return dati
            

def compute_avg_monthly_difference(time_series , first_year , last_year):

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
    #Controllo che la lista ha abbastanza elementi
    if len(time_series) < 2:
        raise ExamException('La lista non ha abbastanza elementi da confrontare!')


    


    #Converto in interi gli anni da considerare
    primo_anno = int(first_year)
    ultimo_anno = int(last_year)
    #Intervallo di anni da considerare
    intervallo = ultimo_anno - primo_anno

    #Creo la lista dei dati passeggeri
    lista_passeggeri = []
    for anno in range(intervallo+1):
        #
        lista_base = [None,None,None,None,None,None,None,None,None,None,None,None]
        lista_base.append(primo_anno + anno)
        lista_passeggeri.append(lista_base)
    
    for argomenti in lista_passeggeri :
        for elemento in time_series :
            dati = elemento[0].split('-')
            if int(dati[0]) == argomenti[-1]:
                argomenti[int(dati[1])-1] = elemento[1]
   
  



    #Calcolo la media per ogni mese:
    lista_finale = []
    mesi = 0
    somma = 0
    while mesi < 12 :
        #Nel caso in cui ci siano dati mancanti faccio sì che la differenza con il precedente e il successivo valga, altrimenti calcolo la differenza tra i dati di due mesi e li inserisco nella somma 
        for anni in range(intervallo):
            if lista_passeggeri[anni][mesi] == None or lista_passeggeri[anni+1][mesi] == None:
                differenza = 0
            else:
                differenza = lista_passeggeri[anni+1][mesi] - lista_passeggeri[anni][mesi]
            somma += differenza
        lista_finale.append(somma)
        somma = 0
        mesi +=1
    #Con un descrittore di lista calcolo la media dividendo ogni elemento della lista per l'intervallo considerato
    lista_finale = [x/intervallo for x in lista_finale]
    return lista_finale



    



time_series_file = CSVTimeSeriesFile(name='data.csv')
#Variabile contenente il risultato di get.data()
time_series = time_series_file.get_data()
print('{}'.format(compute_avg_monthly_difference(time_series, '1949', '1951')))

