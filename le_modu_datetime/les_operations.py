from datetime import timedelta, datetime



jours = timedelta(days=20, hours=-2)
now = datetime.now()
apres_2_jours = now + jours
apres_5_jours = now + timedelta(days=10, hours=-10)


print(now)
print(apres_2_jours)
print(apres_5_jours)

