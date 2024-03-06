# cau c nhap vao mot so nguyen i, thuc hien chen x vao l tai vi tri co so chi muc i.
n=int(input('n='))
L=[]
for i in range (n):
    a=int(input())
    L=L+[a]
#i=int(input('i='))
x=int(input('x='))
#L.insert(i,x)
#print(L)
# c2
# L=L[:i]+[x]+L[:i]
# print(L)
# cau d: thuc hien chen x vao vi tri ke sau vi tri x duoc tim thay trong L, neu x khong ton tai trong L thi chen x vao cuoi L
if x in L:
    k=L.index(x)
    L.insert(k,x)
else:
    L.append(x)
print(L)