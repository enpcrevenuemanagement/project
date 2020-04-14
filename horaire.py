#Definition d'un format pour représenter l'horaire
class Horaire:

    def __init__(self,h,m):
        #Nombre d'heures au format décimal entre minuit et l'horaire considéré
        self.hours=h+m/60
        #Nombre de minutes entre minuit et l'horaire considéré
        self.minutes=h*60+m
        #Valeur normalisée entre 0 et 1
        self.norm = self.hours/24

    def __str__(self):
        return str(self.minutes//60)+":"+str(self.minutes%60)