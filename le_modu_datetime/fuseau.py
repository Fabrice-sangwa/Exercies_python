from datetime import datetime
from zoneinfo import ZoneInfo
import zoneinfo

heure_lubumbashi = datetime.now(tz=ZoneInfo("Africa/Lubumbashi"))
print(heure_lubumbashi)
heure_kinshasa = datetime.now(tz=ZoneInfo("Africa/Kinshasa"))
print(heure_kinshasa)
heure_paris = heure_kinshasa.astimezone(ZoneInfo("Europe/Paris"))
print(heure_paris)