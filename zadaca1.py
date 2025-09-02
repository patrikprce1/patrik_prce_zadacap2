import random
r=7
s=7
matrica=[]

for i in range(r):
    red=[]
    for j in range(s):
        unos=random.randint(1,9)
        red.append(unos)
    matrica.append(red)
#kod iznad kopiran iz proslih zadataka sa vjezbi te nadopnjen potrebnim ispod
zbroj=0
for j in range(s):
    zbroj+=matrica[0][j]  
    zbroj+=matrica[r-1][j]

for i in range(1, r-1):  
    zbroj+=matrica[i][0]
    zbroj+=matrica[i][s-1]

for red in matrica:
    print(red)

print("zbroj rubnih elemenata magtrice iznosi:",zbroj)
