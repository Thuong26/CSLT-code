def nhap():
    n=int(input('n='))
    L=[]
    for i in range(n):
        a=int(input())
        L=L+[a]
    return L
def search(L):
    max=L[0]
    min=L[0]
    for i in range(len(L)):
        if max< L[i]:
            max=L[i]
        if min> L[i]:
            min=L[i]
    return max,min
def inkq(max,min):
    print(max,min)
L=nhap()
max,min=search(L)
inkq(max,min)