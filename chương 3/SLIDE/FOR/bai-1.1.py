n=int(input("n="))
S=1
for i in range (1,n+1,1):
    if n==0: break
    S=S*i
print("n!=",S)