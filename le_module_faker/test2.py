from faker import Faker 

fake =  Faker(locale="fr_FR")


for _ in range (40):
    print("-"*37)
    print(fake.numerify(text="Code : %%#%%-%%%%%-##-%%%%#-##"))
    print(fake.bothify(text="Serie : ??##%%%-###????-####?-##").upper())
