
suma=0
br=0
print("Unesite boj ili =")
while True:
    x=input()

    if x== "=":
        print("Mean value is: "+str (suma/br))
        break
    if int(x)%3==0 and int(x)%5!=0:
        suma +=int(x)
        br+=1
