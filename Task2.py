
def niz(N,M):
    x=[]
    if N<=0:
        return N+M
    elif N>0:
        return N-M
    return niz(M,N-M)
print(niz(15,5))
