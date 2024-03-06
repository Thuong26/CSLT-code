while True:
    n=int(input("n="))
    if 1<=n<=1000000:
       break
s=0
for i in range(1,n+1,2):
    s=s+i
print(s)