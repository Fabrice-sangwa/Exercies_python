
projets = ["pr_MaintenaceHt", "Maintenanceday", "analysesys", "pr_admin et control"]
class Utilisateur :
    
    def __init__(self, name, last_name, matricule):
        self.name = name 
        self.last_name = last_name
        self.matricule = matricule
        
    
    def __str__(self) -> str:
        return f"{self.name} {self.last_name} {self.matricule}"
    
    def afficherprojet(self):
        for projet in projets:
            print(projet)
            
            
class Junior(Utilisateur):
    
    def __init__(self, name, last_name, matricule):
        super.__init__(name, last_name, matricule)
            
johane = Junior("Jahane", "Kasim", "JK001T2022")
mark = Utilisateur("Mark", "Sahid", "MS002I2022")

print(johane)
johane.afficherprojet()        

print("-"*14)

print(mark)
mark.afficherprojet()