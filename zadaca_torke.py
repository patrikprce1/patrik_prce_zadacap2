'''import csv

csv_file_path = 'rezultati_25.csv'

with open(csv_file_path, 'r', encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    data_list = []
    for row in csv_reader:
        data_list.append(row)

ntorke = []
for row in data_list:
    ntorka = row[0], row[1], row[2]
    ntorke.append(ntorka)

for ime, prezime, bodovi in ntorke:
    if int(bodovi) > 49:
        print("Student", ime, prezime, "je polozio ispit!")
'''
import csv

putanja='rezultati_25.csv'
studenti=[]

with open(putanja,'r',encoding="utf-8") as datot:
    citac = csv.reader(datot)
    for red in citac:
        ime=red[0]
        prezime=red[1]
        bodovi=red[2]
        studenti.append((ime, prezime, bodovi))

sortirani_studenti=[]

while len(studenti) > 0:
    najmanji = studenti[0]
    for s in studenti:
        if s[1] < najmanji[1]:
            najmanji = s
    sortirani_studenti.append(najmanji)
    studenti.remove(najmanji)

ocjene = {
    'Nedovoljan':0,
    'Dovoljan':0,
    'Dobar':0,
    'Vrlo dobar': 0,
    'Izvrstan':0
}

for s in sortirani_studenti:
    bod = int(s[2])

    if bod < 50:
        ocjene['Nedovoljan']+=1
    elif bod < 65:
        ocjene['Dovoljan'] +=1
    elif bod < 80:
        ocjene['Dobar'] += 1
    elif bod < 90:
        ocjene['Vrlo dobar'] += 1
    else:
        ocjene['Izvrstan'] += 1

print("Sortirani studenti:")
for s in sortirani_studenti:
    print(s[0], s[1], "-", s[2], "bodova")

print("Ocjene:")
print("Nedovoljan:", ocjene['Nedovoljan'])
print("Dovoljan:", ocjene['Dovoljan'])
print("Dobar:", ocjene['Dobar'])
print("Vrlo dobar:", ocjene['Vrlo dobar'])
print("Izvrstan:", ocjene['Izvrstan'])
