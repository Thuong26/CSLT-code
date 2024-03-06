s=b=[]
n=int(input("n="))
k=int(input("k="))
for i in range(k):
    s.append(0)
    b.append(True)
def inchuoi(s,b,n,k,i):
    for j in range(n):
        if b[j]:
            s[i]=j
            b[j]=False
            if i==k-1: print(s)
            else: inchuoi(s,b,n,i,k+1)
            b[j]=True
inchuoi(s,b,n,i,0)
