 #Modificare l'oggetto CSVFile
 
class CSVFile():

  #inizializzo la classe
    def __init__(self, name):
         self.name = name
         if not isinstance(self.name , str):
             raise Exception("Il nome del file non è una stringa!")

    def get_data(self , start=None , end=None):
        #inizializzo la lista che conterrà le righe richieste 
        data = []  
        #Sanitizzazione start ed end
        if start is not None:
            #contollo che sia una stringa di numeri e in caso la cambio ad un intero
            if type(start) == str and start.isdigit() == True : 
                start = int(start)
            #se è un float lo approsimo ad un intero
            if type(start) == float:
                start = int(start)
            # errore di tipo, generico 
            if not isinstance(start , int):
                raise Exception ("Il dato start : {}, non è del tipo intero, bensì del tipo {}!".format(start,type(start)))
        #Applico gli stessi controlli ad end
        if end is not None:
            if type(end) == str and end.isdigit() == True :
                end = int(end)
            if type(end) == float:
                end = int(end)
            if not isinstance(end , int):
                raise Exception ("Il dato end : {}, non è del tipo intero, bensì del tipo {}!".format(end,type(end)))   
        #Controllo che uno dei due input non sia negativo
        if start<0 or end<0 and (start!=None) and (end!=None):
            raise Exception("Uno dei due input è negativi!!!")
        
         #Apro il mio file, ora posso controllare che il testo da leggere sia abbastanza lungo
        my_file = open('shampoo_sales.txt', 'r')
        #lista delle righe di my_file
        l = my_file.readlines()
        if end > len(l):
            raise Exception("Il file ha troppe poche righe, puoi lefferne al massimo: {}".format(len(l)))
        #Controllo che il valore di end non sia minore di quello di start e in caso li inverto per default, avvisando l'utente
        if start > end and (start!=None) and (end!=None) :
            print("Forse hai invertito l'ordine di start ed end, verranno invertiti per default!")
            x = start
            start = end
            end = x
          
        for line in l:
            elements = line.split(',')
            if elements[0] != 'Date':
                data.append(elements) 

        #ritorno la parte di lista che mi serve 

        data = data[start:end]


        #chiudo il file e return la lista di liste
        my_file.close()
        return data


my_file = CSVFile('shampoo_sales.txt')
print(my_file.get_data(0,3))


class NumericalCSVFile(CSVFile):
    pass

    def get_data(self):
        data = super().get_data()  
        use = []


        for item in data:
            

            for x in item[1:]:
                try:
                    x = float(x)
                    use.append(x)
                except ValueError:    
                    print('il tipo dell\'item è: {}'.format(type(x)))

        return use            

file_p2 = NumericalCSVFile('sales.txt')
#print(file_p2.get_data())