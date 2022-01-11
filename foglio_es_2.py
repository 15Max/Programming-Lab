class Automa():
    def __init__(self, biancheria = None, calzini = None , maglia = None , pantaloni = None , calzatura = None):
        self.biancheria = biancheria
        self.calzini = calzini
        self.maglia = maglia
        self.pantaloni = pantaloni
        self.calzatura = calzatura

    def indossa_biancheria(self):
        self.biancheria = True
        return 1


    