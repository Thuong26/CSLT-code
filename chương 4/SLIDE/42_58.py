
def Nhap():
    n=int(input('n='))
    return n
def nhapdem(n):
    print('nhap',n,'so nguyen')
    t=0
    for i in range(1,n+1):
        m=int(input())
        if m%2==0 and m!=0:
            t=t+1
    return t
def inkq(kq):
    print('so chu so chan la:',kq)
n=Nhap()
kq=nhapdem(n)
inkq(kq)
