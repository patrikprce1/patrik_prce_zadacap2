import re

a=input("Unesi vrijeme alarma(hh:mm:ss): ")

izraz=r"^(?:[0-9]|1[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$"

if re.match(izraz, a):
    print("Unos je ispravan.")
else:
    print("Unos neispravan.")
