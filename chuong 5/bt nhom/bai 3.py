# Hàm delete(L,x) xóa tất cả phần tử có giá trị bằng x trong 
# List L;
n=int(input('n='))
l=[]
ll=[]
for i in range(n):
    a=int(input())
    l=l+[a]
x=int(input('x='))
for i in range(len(l)):
    if l[i]!=x:
        ll=ll+[l[i]]
l=ll.copy()
print(l)