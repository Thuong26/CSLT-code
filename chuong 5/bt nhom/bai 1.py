n=int(input('n='))
l=[]
for i in range(n):
    a=int(input())
    l=l+[a]
k=int(input('k='))
x=int(input('x='))
if k<=len(l):
    l=l[:k]+[x]+l[k:]
else:
    l=l+[x]
print(l)