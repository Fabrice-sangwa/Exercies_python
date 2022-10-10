
from pathlib import Path

p = Path.home().iterdir()

for f in p:
    print(f.name)
    
print("-"*37)

p = Path.home() / "Downloads"

i = 0
for f in p.rglob("*.jpg") :
    print(f.name)
    i += 1
print(i)