class ExamException(Exception):
    pass    



class MovingAverage():
    def __init__(self, length):
        self.length = length
        
        # Controllo che la lunghezza sia un intero
        if  not isinstance(self.length , int):
            raise ExamException("L'input non è un intero!" )
        # Controllo che la lunghezza sia positiva
        if self.length <= 0 :
            raise ExamException('La lunghezza della finestra è negativa o nulla')
        


    def compute(self , series ) :
        
        #Controllo che la serie non sia una lista vuota
        if series == []:
            raise ExamException('La lista contenente la serie è vuota')
        
        #Controllo che la lunghezza della finestra non ecceda quella della serie
        if self.length > len(series):
            raise ExamException('La lunghezza della finestra è più grande di quella della serie')

        # Controllo che gli elementi della serie siano interi 
        for item in series:
            if not isinstance(item, int):
                raise ExamException('Uno degli elementi della lista non è un intero')
        
        
        
        
        #Uso una lista vuota per salvare i risultati della media
        results = []
        # Faccio la media degli elementi richiesti e li salvo in results
        for x in range(len(series)-self.length + 1):
            element = sum(series[x : x+self.length])
            element /= self.length
            results.append(element)
        return results




#MIni-test (not unittesting)

moving_average = MovingAverage(2)
result = moving_average.compute([2,4,8,16])
print(result)
#Controllo che l'attributo length sia proprio 2 
if not moving_average.length == 2 :
    raise ExamException("L'attributo lunghezza non è stato salvato correttamente" ) 
# Utilizzo i dati forniti e controllo che il risultato sia quello atteso
if  not result == [3,6,12]:
    raise ExamException('Il risultato non è quello atteso bensì {}'.format(result))

