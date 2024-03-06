# Hàm search(L,x) tìm x trong List L, nếu tìm thấy thì trả về
# index của x trong L, còn lại trả về None;
n=int(input('n='))
l=[]
for i in range(n):
    a=int(input())
    l=l+[a]
x=int(input('x='))
kt=False
for i in range(len(l)):
    if l[i]==x:
        print(i)
        kt=True
if kt==False:
    print('none')