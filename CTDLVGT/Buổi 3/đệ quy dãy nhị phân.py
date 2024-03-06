S=[]
n=int(input("n="))
for i in range(n):
    S.append(0)
def inchuoi(S,i,n):
    for j in range(0,n-1):
        S[i]=j
        if i==n-1: print(S)
        else: inchuoi(S,i+1,n)
inchuoi(S,0,n)