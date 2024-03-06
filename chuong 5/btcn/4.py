n=int(input('n='))
A=[]
for i in range(n):
    a=int(input())
    A=A+[a]
t=0
for i in range(len(A)):
    if i%2!=0:
        t=t+A[i]
print(t)