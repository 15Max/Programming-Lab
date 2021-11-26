class CSVFile():
    def __init__(self, name):
        self.name = name


    
    def get_data(self):
        data = [] #lista che conterrà le altre liste
        try:
            my_file = open(self.name ,'r')
        except FileNotFoundError: 
            print("Non esiste un file con questo nome : {}!\n".format(self.name))
            print("Il file da aprire è: {}!\n".format("shampoo_sales.txt"))
            my_file = open('shampoo_sales.txt','r')
            
        except Exception as e:
            print("Abbiamo un errore generico, e si trova nel punto: {}".format(e))
            
        for line in my_file:
            elements = line.split(',') #lista cantenente i due elementi splittati
            if elements[0] != 'Date':
                  data.append(elements)
                
        my_file.close()
        return data
        
    
mio_file = CSVFile('shampo_sales.txt')
print(mio_file.get_data())

class NumericalCSVFile(CSVFile):
    pass
    def get_data(self):
        data = []
        for line in my_file:
            elements = line.split(',') #lista cantenente i due elementi splittati
            if elements[0] != 'Date':
                
                elements[1] = float(elements[1])
                data.append(elements)
        

        my_file.close()
        return data
        
        
        
        

file_1 = NumericalCSVFile('shampoo_sales.txt')
print(file_1.get_data())
        

    