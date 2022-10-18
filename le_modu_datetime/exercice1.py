from datetime import date, datetime

une_date = date.fromisoformat("2022-10-15")

print(une_date)
print(type(une_date))

print("-"*37)



date_deux = datetime.strptime("12 Oct 2022", "%d %b %Y")
print(date_deux)

date_trois = datetime.strftime(datetime.now(), "%d %b %Y")
print(date_trois)   


