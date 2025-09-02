import re

unos=input("Unesi string za provjeru: ")

regic = r"^I.*[0-5].*\s.*L$"

podudaranje=re.match(regic, unos)

if podudaranje:
    print("Unos je ispravan ")
else:
    print("Unos ne valja.")
