from lezione8 import Model , IncrementModel


class FitIncrementModel(IncrementModel):
    
    def fit(self , data):
        incr_prev = 0
        previous = data[0]
        #Faccio il calcolo degli incrementi esclusi gli ultimi tre mesi
        for item in data:
            incr_prev += (item - previous)
            previous = item

        avg_increment =  incr_prev/ (len(data)-1)
        self.global_avg_increment = avg_increment
    # Presuppongo di dare in input soltanto gli ultimi tre mesi
    def predict(self , data):
        #
        predict = super().predict(data)
        predict -= data[-1]
        try :
            prediction = (predict + self.global_avg_increment)/2 + data[-1]
        except:
            print("Non hai effettuato il fit, la vecchia prediction era: ")
            prediction = predict + data[-1]
        return prediction


dati = [52,60,67]
fit_dati = [8,19,31,41,50]   
fit_increment_model = FitIncrementModel()
fit_increment_model.fit(fit_dati)
print("{}".format(fit_increment_model.predict(dati))) 

        




        