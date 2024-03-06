def nhap():
    n=int(input('n='))
    L=[]
    for i in range(n):
        a=int(input())
        L=L+[a]
    return L
def tgt(L):
    t=0
    for i in range(len(L)):
        if i%2!=0:
            t=t+L[i]
    return t
def inkq(t):
    print(t)
L=nhap()
t=tgt(L)
inkq('Tong='+str(t))
