def nhap():
    a = float(input("a="))
    b = float(input("b="))
    t = input("Toan tu:")
    return a, b, t

def thuchien(a, b, t, kq):
    if t == '+':
        kq = a + b
    elif t == '-':
        kq = a - b
    elif t == '/' and b != 0:
        kq = a / b
    elif t == '*':
        kq = a * b
    return kq

def in_kq(a, b, t, kq):
    print(f"{a}{t}{b}={kq}")

a = 0
b = 0
kq = 0
t = 'k'

while True:
    a, b, t = nhap()
    kq = thuchien(a, b, t, kq)
    in_kq(a, b, t, kq)

    kt = input("Tiep tuc: ").lower()
    if kt == 't':
        break
