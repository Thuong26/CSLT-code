n=int(input('n='))
L=[]
K=[]
for i in range(n):
    a=int(input())
    L=L+[a]
L.reverse()
K=L.copy()
print(K)
K.sort()
print(K)
    