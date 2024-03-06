from tkinter import N
def nhap():
    print('Nhap mot so nguyen:')
    n=int(input('n='))
    return n
def tinh(n):
    S=0
    for x in range(1,n+1):
        S=S+x
    return S
def inkq(n,S):
    print('Tong cua ',n,' so nguyen duonng dau tien=',S,sep='')
n=nhap()
S=tinh(n)
inkq(n,S)