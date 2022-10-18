class Person : 
    
    def __init__(self, name, last_name, age) :
        self.name = name 
        self.last_name = last_name
        self.age = age
        
    def __str__(self) -> str:
        return f"Nom : {self.name}\nPost Nom:{self.last_name}\nAge: {self.age}"
    
    
james = Person("James", "Kubernetes", 33)
print(james)