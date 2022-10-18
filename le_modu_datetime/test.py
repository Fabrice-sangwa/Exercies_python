from datetime import date, time, datetime

from dateutil import parser
import dateparser


print(time())

print(datetime.today())
print(date.today())
print(datetime.now())


print("-"*37)

now = datetime.now()
print(now.hour)
print(now.minute)
print(now.second)

print("-"*37)


une_date = parser.parse("24 october 2022 at 9 am 18 minutes 45 seconds")
print(une_date)

aujourdhui = dateparser.parse("aujourd'hui")
demain = dateparser.parse("demain")
mois_passe = dateparser.parse("Il y a un mois")

print(aujourdhui)
print(demain)
print(mois_passe)
