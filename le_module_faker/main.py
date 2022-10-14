from pprint import pprint
from faker import Faker
from faker import Faker

fake = Faker(locale="fr_FR")


print(fake.unique.name())
print(fake.address())
print(fake.phone_number())
phrase = fake.text()
print(phrase)

