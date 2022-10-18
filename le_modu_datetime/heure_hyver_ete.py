from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


montreal_tz = ZoneInfo("America/Montreal")
march_7 = datetime(2020, 3, 7, 18, 0, 0, tzinfo=montreal_tz)
march_8 = datetime(2020, 3, 8, 18, 0, 0, tzinfo=montreal_tz)

print(march_7)
print(march_8)

print("-"*25)

print(march_7.tzname())
print(march_8.tzname())

print("-"*25)

montreal_tz = ZoneInfo("America/Montreal")
march_7 = datetime(2020, 3, 7, 18, 0, 0)
march_7_utc = march_7.astimezone(ZoneInfo("UTC"))

march_8 = march_7_utc + timedelta(days=1)
march_8 = march_8.astimezone(montreal_tz)

print(march_7)
print(march_7_utc)
print(march_8)