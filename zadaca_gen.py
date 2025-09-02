def parni(n):
    for i in range(n):
        if i%2==0:
            yield i

def neparni(n):
    for i in range(n):
        if i%2!=0:
            yield i

unos=int(input("unesi granicu provjere"))
parni_l=[]
neparni_l=[]
for broj in parni(unos):
    parni_l.append(broj)

for broj in neparni(10):
    neparni_l.append(broj)

print("Parni brojevi",parni_l)
print("Neparni brojevi",neparni_l)
