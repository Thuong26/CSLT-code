n=int(input("n="))
i=1
while i<=n:
    # In (n-i) dấu cách ở dòng i
    k=1
    while k<=(n-i):
        print(" ",end="")
        k=k+1  
    # Ở dòng thứ i sẽ có (2*i-1) dấu * 
    j=1
    while j<= (2*i-1):
        print("*",end="")
        j=j+1
    print()
    i=i+1