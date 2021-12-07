class Model():
    def fit(self , data):
        raise NotImplementedError('Metodo non implementato')

    def predict(self , data) :
        raise NotImplementedError('Metodo non implementato')
 


class IncrementModel(Model):


    def predict(self,data):
        #Controllo che data sia effettivamente una lista
        if type(data) != list:
            raise TypeError ("l'argomento data dato in input non  è una lista!")
        #Controllo che data non sia una lista vuota
        if data == None:
            raise Exception ("La lista dei dati è vuota!")
        #Controllo che ci siano almeno due mesi nella lista
        length = len(data)
        if length < 2:
            raise Exception( "Non ci sono abbastanza dati nella lista per implementare questo modello!")
        
        #Controllo che gli elementi della lista siano effettivamente numeri e sanitizzo nel caso in cui ci sia una string acontenente un numero
        for item in data:
            # Se ho una stringa contenente un intero cambio il tipo
            if isinstance(item,str) and item.isdigit() :
                item = int(item)
            #se ho una stringa contenente un float 
            pass
                


        

        #Creo una variabile di appoggio per salvare la somma degli incrementi
        prediction = 0
        #Creo una variabile che conterrà il valore precedentemente analizzato nel ciclo
        previous = data[0]
        #Per ogni elemento di una lista a partire dal secondo, aggiungerò la differnza con l'elemento precedente alla somma degli incrementi e poi lo indicherò come elemento precedente 
        for item in data[1:]:
            prediction += (item - previous)
            previous = item
        
        #divido la somma degli incrementi per il numero di mesi considerati
        prediction = prediction / (length-1)
        # Aggiungo all'ultimo elemento della lista, che indica il valore di vendite attuale la media degli incrementi
        prediction += data[length-1] 
        return prediction


dati = [50,52,60]

increment_model = IncrementModel()
print("{}".format(increment_model.predict(dati)))
