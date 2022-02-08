#Creo una classe per le eccezioni
class ExamException(Exception):

        pass


#Creo la classe CSVTimeSeriesFile
class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name
    
    def get_data(self):
        #lista che conterrà le altre liste
        data = []
        #Apro il file per la lettura 
        my_file = open(self.name ,'r')

        # leggo le righe del file
        for line in my_file:
            #lista contenente i due elementi splittati
            elements = line.split(',')
            #Tolgo l'elemento new line (/n)
            elements[-1] = elements[-1].strip()
            #Se non sto leggendo l'intestazione
            if elements[0] != 'date':
                #Trasformo tutti i dati dei passegeri in interi
                elements[1] = int(elements[1])
                # aggiungo i vari elementi nella lista di liste
                data.append(elements)
                
        my_file.close()
        return data




# Creo la funzione richiesta 
def compute_avg_monthly_difference(time_series, first_year, last_year):

    #Converto in interi gli anni da considerare
    first_year = int(first_year)
    last_year = int(last_year)
    #Intervallo di anni da considerare
    n = last_year - first_year
    # Lista anni
    lista_anno = []
    # Creo la lista degli anni
    for i in range(n+1):
        lista_anno.append(first_year + i)

    # Creo una lista dei dati da analizzare:
    #tramite un descrittore di lista creo una lista di liste contenenti i dati dei passeggeri divisi per anni, otterò quindi un numero di sottoliste pari agli anni presi in considerazione

    data = [[element[1] for element in time_series if element[0].startswith(str(year))] for year in lista_anno]
    # Sempre tramite i descrittori di lista sommo con la funzione sum sulle liste tutte le differenze per mese 
    lista_ausiliaria = [sum([data[i+1][month] - data[i][month] for i in range(n)]) for month in range(12)]
    #Con un descrittore di lista 
    lista_finale = [x/n for x in lista_ausiliaria]
    return lista_finale


time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
print('{}'.format(compute_avg_monthly_difference(time_series, '1949', '1951')))21
