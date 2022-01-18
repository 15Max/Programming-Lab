

class CSVFile():
    def __init__(self, name):
        self.name = name
    
    def get_data(self):
        data = [] #lista che conterrà le altre liste
        my_file = open(self.name ,'r')
        for line in my_file:
            elements = line.split(',') #lista cantenente i due elementi splittati
            if elements[0] != 'Date':
                  data.append(elements)
                
        my_file.close()
        return data
        
    
mio_file = CSVFile('shampoo_sales.txt')
print(mio_file.get_data())