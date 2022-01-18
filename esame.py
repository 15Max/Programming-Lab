class ExamException(Exception):
   pass

class Diff():
    def __init__(self, ratio=1):
        self.ratio = ratio 
        #Controllo che ratio sia un numero
        if not isinstance(ratio , int) and not isinstance(ratio , float):
            raise ExamException('Il parametro ratio inserito non è un numero!')
        
        #Controllo che ratio sia diverso da zero
        if self.ratio <= 0:
            raise ExamException('Ratio non deve essere minore o uguale a zero')


    def compute(self, input_list) :
        #Controllo che l'input sia effettivamente una lista
        if not isinstance(input_list, list):
            raise ExamException("L'input non è una lista!" )
        #Se l'input è una lista controllo che questa non sia vuota
        elif input_list == []:
            raise ExamException('La lista degli input è vuota')
        else:
            #Controllo che la lista abbia almeno due elementi
            if len(input_list) < 2:
                raise ExamException('La lista ha meno di due elementi')
            # Contollo che la lista contenga numeri
            for item in input_list:
                if not isinstance(item,int) and not isinstance(item,float):
                    raise ExamException('Uno degli elementi della lista non è un numero!')

       


        #creo una lista vuota in cui inserire i risultati
        results = []

        for index in range(len(input_list)-1):
            #Calcolo la differenza degli elementi nella lista
            element = input_list[index+1] - input_list[index]
            #Se il paramtro ratio è stato inserito 'riscalo' l'elemento ottenuto
            element /= self.ratio
            #Inserisco l'elemento calcolato nella lista dei risultati
            results.append(element)

        return results




            