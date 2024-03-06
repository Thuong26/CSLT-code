n=int(input('n='))
if 0<=n<=100:
    giaithua=1
    for i in range(1,n+1): 
        giaithua=giaithua*i
    print(str(n)+'!='+str(giaithua))
else: print()