def Nhap():
    n = int(input("Nhap n = "))
    return n
def LaSNT(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
def InSoNguyenTo(n):
    for i in range(2, n+1):
        if LaSNT(i):
            print(i, end=' ')
n=Nhap()
print('Cac so nguyen to khong qua', n,'la:')
InSoNguyenTo(n)

