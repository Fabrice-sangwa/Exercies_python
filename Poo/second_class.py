from pprint import pprint


class Voiture:
    marque = "Porsche"
    
porsche = Voiture()
print(porsche.marque)

lamborgini = Voiture()
print(lamborgini.marque)

print("-"*15)

Voiture.marque = "Nissan"

voiture_01 = Voiture()
voiture_02 = Voiture()

print(voiture_01.marque)
print(voiture_02.marque)

print("-"*15)

voiture_01.marque = "Jeep"
voiture_02.marque = "Mercedes"

print(voiture_01.marque)
print(voiture_02.marque)

print("-"*15)
