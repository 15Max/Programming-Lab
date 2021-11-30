 #Modificare l'oggetto CSVFile
 
class CSVFile():
  #inizializzo la classe
    def __init__(self, name):
         self.name = name
         if not isinstance(self.name , str):
             raise Exception("Il nome del file non è una stringa!")

    def get_data(self , start=None , end=None):
        #pulizia del dato
        if start > end:
            raise
        #Sanitizzazione 
        if type(start) == str:
            if start.isdigit() == True : 
                start = int(start)
        
        if type(start) == float:
            start = int(start)

        if type(end) == str:
            if start.isdigit() == True : 
                start = int(start)
        
        if type(end) == float:
            start = int(start)
        # errore generico
        if not isinstance(start , int):
            raise Exception ("Il dato start : {}, non è del tipo intero!")

        if not isinstance(end , int):
            raise Exception ("Il dato end : {}, non è del tipo intero!")
        
        if not isinstance(self.name , str):
            raise Exception ("Il dato start è una stringa")


        



        
            my_file = open('shampoo_sales.txt', 'r')
        
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
print(my_file.get_data(1,2))


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
print(file_p2.get_data())