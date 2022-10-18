class Personne:
    
    def __init__(self, name, last_name, age) -> None:
        self.name = name
        self.last_name = last_name
        self.age = age
        
    def profession(self):
        return "C'est un homme"
        
        
    def __str__(self) -> str:
        return f"{self.name} {self.last_name} {self.age} ans"
        
    
class Enseignant(Personne):

    def profession(self):
        super().profession()
        return "C'est un Enseignant"


class Medecin(Personne):
    
    def profession(self):
        #super().profession()
        return "C'est un Medecin"
        


good_doctor = Medecin("Shaun", "Murphy", 30)
print(good_doctor)
print(good_doctor.profession())

print("-"*20)

skin = Enseignant("Skin", "Du bois", 59)
print(skin)
print(skin.profession())

print("-"*20)

james = Personne("James", "Sekti", 36)
print(james)
print(james.profession())
