from datetime import date, time, datetime


today = date(year=2022, month=10, day=15)

hour = time(hour=20, minute=32, second=12)

print(today)
print(hour)
print("-"*37)

aujourdhui = datetime.today() 
la_date = date.today()


print(aujourdhui)
print(aujourdhui.hour)
print(la_date)

print("-"*37)

today = date.today()
tomorrow = today.replace(day=today.day + 1) 

print(today)
print(tomorrow)

print("-"*37)

this_month = date.today()
two_month_after = this_month.replace(month=this_month.month + 2)

print(this_month)
print(two_month_after)

print("-"*37)  