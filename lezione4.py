#In place and not in place <---- Look at Python notes, don't work in place?

import random
class Person():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return 'Person: "{} {}"'.format(self.name, self.surname)

    def say_hi(self):
        random_number = random.randint(0,2)

        if random_number == 0 :
            print("Hello, I am {}")






person1 = Person('Mario','Rossi')
person2 = Person('Marta', 'Lucas')
print(person1)
print(person1.name)
print(person1.surname)
 

#Definisco la classe Person, quando la voglio estendere farò in modo che alcune caratteristiche vengano ereditate inserendo tra parentesi nella definizione il nome della classe da cui volgio ereditare. Poi posso sovrascrivere i metodi che voglio modificare
# con super (superclasse)  richiamo la funzione della classe genitrice, anche se avevo sovrascritto quest'ultima nella nuova classe 


