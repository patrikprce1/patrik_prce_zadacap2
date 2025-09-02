import random

ucenici=['Ivan', 'Antonio', 'Antonija', 'Anto', 'Marijan', 'Zvjezdan', 'Ivan', 'Mihaela', 'Ružica', 'Dorijan', 'Petra',
'Matej', 'Filip', 'Magdalena', 'Mate', 'Iva', 'Danis', 'Josip', 'Nebojša', 'Ante', 'Luka', 'Ante', 'Lorena', 'Ivan', 'Nikola',
'Ivan', 'Helena', 'Ivan', 'Gabrijela', 'Andrija', 'Regina', 'Petar', 'Dino', 'Marija', 'Semir', 'Gabriela', 'Borna', 'Filip', 'Krešimir', 'Ivana',
'Gabrijel', 'Vinko', 'Vinko', 'Romana', 'Viktorija', 'Mija', 'Matej', 'Vinko', 'Luka', 'Antea', 'Ivan', 'Ivan', 'Luka', 'Daniel', 'Nikola', 'Marko']

rij=dict()
print(len(ucenici))

for ucenik in ucenici:
    rij[ucenik]=random.randint(1,5)
print(len(rij))
print(rij)
#dogodi se da ako stavimo da je ime key znacu da ako su ista imena da ih registrira kao jedno
#pa nisam siguran kako da to izbjegnemo

broj_ocj=dict()
for i in rij.values():
    if i in broj_ocj:
        broj_ocj[i]+=1
    else:
        broj_ocj[i]=1
print(broj_ocj)
brojac=0
for ocjena in rij.values():
    if ocjena>1:
        brojac+=1
print("Broj ucenika s pozitivnom ocjenom:" , brojac)

prolaznost=brojac/len(ucenici)*100
print("Prolaznost je",prolaznost, "%")
