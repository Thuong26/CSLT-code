n=int(input())
L=[]
for i in range (0,n):
    m=int(input())
    L=L+[m]
S=0
P=[]
for i in range(0,len(L)):
    if L[i]==0:
        S+=1
    else:
        P=P+[S]
        S=0
if max(P)==0:
    print("No")
else:
    print(max(P))
