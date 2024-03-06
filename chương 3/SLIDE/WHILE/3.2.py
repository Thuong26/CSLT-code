n=int(input("n="))
if n>=1 and n<=50:
    i=1
    while i<=n:
        if i%10==0:
            print(i)
        else: print(i,end=" ")
        i=i+1 
else : print('Nhap lai')