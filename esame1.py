
#Creo una classe per le eccezioni
class ExamException(Exception):

        pass


#Creo la classe CSVTimeSeriesFile
class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name

        #Provo ad aprire il file e leggere una riga
        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False
            
    
    #Definisco il metodo get_data richiesto
    def get_data(self):
        #Controllo che il file sia leggibile
        if not self.can_read:
            raise ExamException('Il file non è leggibile!')
        #Apro il file per la lettura 
        my_file = open(self.name ,'r')



        #lista che conterrà le altre liste
        data = []

        #controllo l'esistenza del file?

        # leggo le righe del file
        for line in my_file:
            #lista contenente gli elementi della riga splittati
            elements = line.split(',')
            #Tolgo l'elemento new line (/n)
            elements[-1] = elements[-1].strip()
            #Se non sto leggendo l'intestazione
            if elements[0] != 'date':
                
            
                #Trasformo tutti i dati dei passegeri in interi
                elements[1] = int(elements[1])
                # aggiungo i vari elementi nella lista di liste
                data.append(elements)
        #Chiudo il file        
        my_file.close()
        return data




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

    # Creo una lista dei dati da analizzare:
    #tramite un descrittore di lista creo una lista di liste contenenti i dati dei passeggeri divisi per anni, otterò quindi un numero di sottoliste pari agli anni presi in considerazione

    dati = [[elemento[1] for elemento in time_series if elemento[0].startswith(str(anno))] for anno in lista_anno]
    # Sempre tramite i descrittori di lista sommo con la funzione sum sulle liste tutte le differenze per mese 
    lista_ausiliaria = [sum([dati[i+1][mese] - dati[i][mese] for i in range(n)]) for mese in range(12)]
    #Con un descrittore di lista divido ogni elemento per l'intervallo di anni considerato, ottenendo la media richiesta
    lista_finale = [x/intervallo for x in lista_ausiliaria]
    return lista_finale


time_series_file = CSVTimeSeriesFile(name='data.csv')
#Variabile contenente il risultato di get.data()
time_series = time_series_file.get_data()
print('{}'.format(compute_avg_monthly_difference(time_series, '1949', '1951')))
