def nhap():
    L=[]
    for i in range(10):
        a=int(input())
        L=L+[a]
    K=L.copy()
    return L,K
def hoan(L,K):
    for i in range(0, 10, 2):
        K[i] = L[i + 1]
        K[i + 1] = L[i]
    return K
def inkq(K):
    for i in K:
        print(i,end=' ')
L,K=nhap()
K=hoan(L,K)
inkq(K)
