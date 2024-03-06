# cho 1 list L gom 7 so nguyen
# Nhap mot so nguyen x, tim vaf xoa tat ca cca phan tu co gia tri=x trongL
L=[]
n=7
for i in range (n):
    a=int(input())
    L=L+[a]
x=int(input())
while x in L:
    L.remove(x)
print(L)