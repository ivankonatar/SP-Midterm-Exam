
def insert():
    x = [1, 2, 4, 5, 6, 7, 8]
    y = []
    n=input("Unesite n: ")
    br=0
    for i in range (len(x)-1):
        if int(n)>=x[i] and int(n)<x[i+1]:
            y.append(x[i])
            y.append(int(n))
            br+=1
        else:
            y.append(x[i])
            br+=1
    print("slozenost: ",br)
    return y
print(insert())
