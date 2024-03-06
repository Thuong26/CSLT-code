from re import A
n=int(input('n='))
L=[]
for i in range (n):
    a=int(input())
    L.append(a)
#cau a
x=int(input('x='))
if x in L:
    print(L.index(x))
else: print('khong tim thay')
#cau b: in len man hinh so chi muc cua tat ca cac phan tu dau gia tri bang x trong L
for i in range(n):
    if L[i]==x:
         print(i)
