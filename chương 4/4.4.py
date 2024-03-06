from re import A
def nhap():
    print('Nhap 3 so nguyen:')
    a=int(input('a='))
    b=int(input('b='))
    c=int(input('c='))
    return a,b,c
def max3(a,b,c):
    kq=a
    if b>a and b>c: kq=b
    elif c>a and c>b: kq=c
    return kq
def inkq(kq):
    print('So lon nhat la: '+str(kq))
a,b,c=nhap()
kq=max3(a,b,c)
inkq(kq)