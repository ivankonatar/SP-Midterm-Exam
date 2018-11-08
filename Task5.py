
n = int(input("Unesite broj kolona i vrsta jedinicne matrice: "))
x=[]
proizvod_glavne=1
proizvod_sporedne=1
for i in range(n):
    x.append([])
    for j in range(n):
        broj = int(input("Unestite broj : "))
        x[i].append(broj)
        if i==j:
            proizvod_glavne*=broj
for i in range(n):
    for j in range(n):
        if (i+j)==(n-1):
            proizvod_sporedne*=x[i][j]
for vektor in x:
    print(vektor)
print("`products` of the elements on the `main` matrix diagonal is:  ", proizvod_glavne)
print("`products` of the elements on the `secondary` matrix diagonal is:  ", proizvod_sporedne)
print("Zbir glavne i sporedne je:",proizvod_sporedne+proizvod_glavne)
