def nhap():
    n=int(input('n='))
    L=[]
    for i in range(n):
        a=float(input())
        L=L+[a]
    return L
def SL(L):
    dem=0
    d=0
    tb=0
    tbc=0
    for i in range(len(L)):
        if L[i]>0: dem=dem+1
    for i in range(len(L)):
        if L[i]%2==0: 
            d=d+1
            tb=(tb+L[i])
            tbc=tb/d
    return dem,tbc
def inkq():
    print('SND='+str(dem))
    print('TBC='+str(tbc))
L=nhap()
dem,tbc=SL(L)
inkq()

    