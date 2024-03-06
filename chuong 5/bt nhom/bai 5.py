from re import L
def nhap():
    n=int(input())
    L=[]
    for i in range(n):
        a=int(input())
        L=L+[a]
    x=int(input('x='))
    y=int(input('y='))
    return L,x,y
def update(L,x,y):
    if x in L:
        for i in range(len(L)):
            if L[i]==x:
                m=i
        L=L[:m]+[y]+L[m:]
    return L
def inkq():
    M=[]
    for i in range(len(L)):
        if x!=L[i]:
            M.append(L[i])
    print(M)
L,x,y=nhap()
L=update(L,x,y)
inkq()