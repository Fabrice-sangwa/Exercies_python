
from faker import Faker 

fake =  Faker(locale="fr_FR")

for i in range(1,31):
    print("-"*37)
    print("Nom :" ,fake.unique.name())
    print("Boulot :", fake.unique.job())
    print("Fichier :" ,fake.unique.file_path(depth=4, category="video"))      
    print("Info carte :", fake.credit_card_number(), fake.credit_card_expire(), fake.credit_card_security_code())
    print("Couleur Préférée :", fake.rgb_color())
    print("Team color :",  fake.hex_color())
