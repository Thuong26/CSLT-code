N=int(input())
A=[]
for i in range(1,N+1):
    A=A+[int(input())]
# N=6
# A=[2,3,4,5,6,7]
# N=7
# A=[-1,3,-2,4,5,-6,7]
# N=6
# A=[1,2,0,-4,5,6]
# N=5
# A=[1,-2,3,-4,5]
t=0
a=0
b=0
for i in range(1,len(A)):
    b=b+1
    while A[i]*A[i-1]<0:
        if A[i]*A[i-1]<0:
            t=t+1
        i=i+1
        a=1
        b=b+1
        if i==len(A):
            break
    if a==1: break
if b!=len(A)-1 or t==len(A)-1: print(t+1)
if b==len(A)-1: print('0')