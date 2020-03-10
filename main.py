
#Définition des horaires des vols

class time:

    def init(self,h,m):
        self.hours=h
        self.minutes=m

    def convert_to_hour(self):
        return self.hours+self.minutes/60

