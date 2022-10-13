from telnetlib import NAOL


a = 4
b = 0

try :
    division = a / b
    print(division)
except ZeroDivisionError:
    print("Division  par 0 impossible")
except TypeError:
    print("Mauvais type")
except NameError :
    print("Une valeur pas définie")
finally :
    print("Find du programme")
