for i in range(1,10):
    for k in range(1,10-i):
        print(" ",end="")
    for j in range(0,2*i-1): 
        print("*",end="")
    print()