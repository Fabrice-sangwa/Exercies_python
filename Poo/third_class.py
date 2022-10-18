

class Person:
    
    count_person = 0
    
    def __init__(self, name, last_name, age):
        self.name = name 
        self.last_name = last_name
        self.age = age
        Person.count_person += 1

jo = Person("Jo", "Simon", 32)

print("Name :", jo.name)
print("Last Name :", jo.last_name)
print("Age :", jo.age)
print("Person created :", Person.count_person)

print("-"*15)

sun = Person("Peter", "sun", 22)
print("Name :", sun.name)
print("Last Name :", sun.last_name)
print("Age :", sun.age)
print("Person created :", Person.count_person)

print("-"*15)



