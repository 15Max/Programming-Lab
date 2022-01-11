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
        
        # Se la lista non è vuota, e solo allora , posso procedre con gli altri controlli
        if not series == []:
            #Controllo che la lunghezza della finestra non ecceda quella della serie
            if self.length > len(series):
                raise ExamException('La lunghezza della finestra è più grande di quella della serie')
            # Controllo che gli elementi della serie siano numeri
            for item in series:
                if not isinstance(item, int) or not isinstance(item,float):
                    raise ExamException('Uno degli elementi della lista non è un numero')
        
        
        
        
        #Uso una lista vuota per salvare i risultati della media
        results = []
        # Faccio la media degli elementi richiesti e li salvo in results
        for x in range(len(series)-self.length + 1):
            element = sum(series[x : x+self.length])
            element /= self.length
            results.append(element)
        return results





