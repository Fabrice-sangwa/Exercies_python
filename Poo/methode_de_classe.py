class Voiture: 
    
    nombre_de_voiture = 0
    
    def __init__(self, marque, vitesse, serie, prix):
        self.marque = marque
        self.vitesse = vitesse
        self.serie = serie
        self.prix = prix
        Voiture.nombre_de_voiture += 1
        
        
    @classmethod
    def lamborghini(cls):
        return cls(marque="Lamborghini", vitesse=400, serie=2020, prix=145_000)
    
    @classmethod
    def peugeot(cls):
        return cls(marque="Peugeot", vitesse=900, serie=2022, prix=200_000)
    
    @staticmethod
    def afficher_nombre_de_voiture():
        print(f"Vous avez {Voiture.nombre_de_voiture} voitures dans votre garrage.")
    
    def afficher(self):
        print(f"Marque: {self.marque}\nVitesse: {self.vitesse} km/h\nSerie: {self.serie}\nPrix: {self.prix}$")


nissan = Voiture(marque="Nissan", vitesse=240, serie=2021, prix=49_000)  
nissan.afficher()  

print("-"*15)

peugeot_01 = Voiture.peugeot()
peugeot_01.afficher()

print("-"*15)

Voiture.afficher_nombre_de_voiture()
