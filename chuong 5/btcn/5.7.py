from os import remove
def nhap():
    n=int(input('n='))
    L=[]
    for i in range(n):
        a=int(input())
        L=L+[a]
    return L
def xoa(L):
    K=[]
    for i in range(len(L)):
        if L[i] not in K:
            K.append(L[i])
    return K
def inkq(K):
    for i in range(len(K)):
        print(K[i],end=' ')
L=nhap()
K=xoa(L)
inkq(K)
