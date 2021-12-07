 #Modificare l'oggetto CSVFile
 
class CSVFile():

  #inizializzo la classe
    def __init__(self, name):
        self.name = name
        #Contollo di aprire un file del formato corretto
        if not self.name[-4:] == '.txt' and not self.name[-4:] == '.csv':
            raise Exception('Il formato del file è errato!')
        
        #Contollo di aprire un file che esista?

        #Controllo che il nome del file sia una stringa
        if not isinstance(self.name , str):
            raise Exception("Il nome del file non è una stringa!")
        #se il nome del file da aprire non è quello giusto alzo un'eccezione
        if self.name != "shampoo_sales.txt":
            raise Exception('Hai aperto il file sbalgiato!')

        
        
        
    

    def get_data(self , start=None , end=None):
         #inizializzo la lista che conterrà le righe richieste 
            data = [] 
            #Sanitizzazione start ed end
            if start is not None:
                #contollo che sia una stringa contenente un numero intero e in caso la cambio ad un intero
                if type(start) == str and start.strip().isdigit() == True : 
                    start = int(start)
                #contollo che sia una stringa contenente un numero float e in caso la cambio ad un intero
                if type(start) == str and start.count('.') == 1 and start.replace('.','').strip().isdigit() == True:
                    start = int(float(start))
                    #se è un float lo approsimo ad un intero
                if type(start) == float:
                    start = int(start)
                # errore di tipo, generico 
                if not isinstance(start , int):
                    raise Exception ("Il dato start : {}, non è del tipo intero, bensì del tipo {}!".format(start,type(start)))
                #Controllo che start non sia negativo
                if start<0:
                    raise Exception("Start è negativo!")
            #Applico gli stessi controlli ad end
            if end is not None:
                if type(end) == str and end.strip().isdigit() == True :
                    end = int(end)
                if type(end) == float:
                    end = int(end)
                if type(end) == str and end.count('.') == 1 and end.replace('.','').strip().isdigit() == True:
                    end = int(float(end))
                if not isinstance(end , int):
                    raise Exception ("Il dato end : {}, non è del tipo intero, bensì del tipo {}!".format(end,type(end)))
                if end<0:
                    raise Exception("End è negativo!")
            #Apro il mio file, ora posso controllare che il testo da leggere sia abbastanza lungo
            my_file = open(self.name, 'r')
           
            #lista delle righe di my_file
            l = my_file.readlines()
            if end != None and end > len(l):
                my_file.close()
                raise Exception("Il file ha troppe poche righe, puoi leggerne al massimo: {}".format(len(l)))
            #Controllo che il valore di end non sia minore di quello di start e in caso li inverto per default, avvisando l'utente
            if (start!=None) and (end!=None) and start > end :
                print("Forse hai invertito l'ordine di start ed end, verranno invertiti per default!")
                x = start
                start = end
                end = x
            #Separo gli elementi delle righe del mio file e inserisco dentro a data
            for line in l:
                elements = line.split(',')
                if elements[0] != 'Date':
                    data.append(elements) 

             #ritorno la parte di lista che mi serve
            if start== None and end != None:
                data = data[:end] 
            elif start != None and end == None:
                data = data[start:]
            elif start != None and end !=None:
                data = data[start:end]

            #chiudo il file e return la lista di liste
            my_file.close()
            return data
   


my_file = CSVFile('shampoo_sales.txt')
print(my_file.get_data('0 ',3.0))


class NumericalCSVFile(CSVFile):
    def get_data(self, start = None, end = None):
        #Utilizzo la funzione get data definita nella classe genitrice per recuperare la lista su cui lavorare
        data = super().get_data(start, end)  
        use = []
        for item in data:
            for x in item[1:]:
                try:
                    x = float(x)
                    use.append(x)
                except ValueError:    
                    print('il tipo dell\'item è: {}'.format(type(x)))

        return use
        #metodi aggiuntivi che potrebbero essere utili
    def total(self , start = None, end = None):
        l = self.get_data(start,end) 
        return sum(l)
    def average(self, start = None , end = None):
        return self.total(start,end)/(end-start)
              

file_p2 = NumericalCSVFile('shampoo_sales.txt')
#print(file_p2.get_data(0,4))
#print(file_p2.total(0,4))
#print(file_p2.average(0,4))