 #Modificare l'oggetto CSVFile
 
class CSVFile():
  #inizializzo la classe
    def __init__(self, name):
         self.name = name
         if not isinstance(self.name , str):
             raise Exception("Il nome del file non è una stringa!")

    def get_data(self , start=None , end=None):
        #Sanitizzazione start ed end
        if type(start) == str:
            if start.isdigit() == True : 
                start = int(start)
        
        if type(start) == float:
            start = int(start)

        if type(end) == str:
            if end.isdigit() == True : 
                end = int(end)
        
        if type(end) == float:
            end = int(end)
        
        if start > end:
            print("Forse hai invertito l'ordine di start ed end, verranno invertiti per default!")
            x = start
            start = end
            end = x
        
        if start<0 or end<0:
            raise Exception("Uno dei due input è negativi!!!")

        
        
        
        # errore generico
        if not isinstance(start , int):
            raise Exception ("Il dato start : {}, non è del tipo intero!".format(start))

        if not isinstance(end , int):
            raise Exception ("Il dato end : {}, non è del tipo intero!".format(end))
        
        if not isinstance(self.name , str):
            raise Exception ("Il dato start è una stringa")
         #Apro il mio file, ora posso controllare che il testo da leggere sia abbastanza lungo
        my_file = open('shampoo_sales.txt', 'r')
        if my_file.readlines() < end : 
            raise Exception("Il file non ha abbastanza righe da leggere!")

        
        #inizializzo futura la lista di liste
        finish_list = []
        
        


        


        for line in my_file:
            #split gli element 
            elements = line.split(',')
            #aggiungo ogni lista nella lista finale
            if elements[0] != 'Date':
                finish_list.append(elements) 

        #ritorno la parte di lista che mi serve 

        finish_list = finish_list[start:end]
      #chiudo il file e return la lista di liste
        my_file.close()
        return finish_list


my_file = CSVFile('shampoo_sales.txt')
print(my_file.get_data("7","4"))


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