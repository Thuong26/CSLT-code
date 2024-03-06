def nhap():
    n=int(input('n='))
    L=[]
    for i in range(n):
        a=int(input())
        L=L+[a]
    x=int(input('x='))
    return L,n,x
def daucuoi(L):
    K=[]
    K.append(L[0])
    K.append(L[-1])
    return K
def ktra(L,x):
    Kt=True
    if x in L: 
        kt=True
    else: kt= False
    return kt
def inkq(K,kt):
    print(K)
    print(kt)
L,n,x=nhap()
K=daucuoi(L)
kt=ktra(L,x)
inkq(K,kt)


