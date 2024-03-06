def nhap():
    n=int(input("n="))
    return n
def inkq(n):
    for i in range (2,n+1,2):
        print(i,end=" ")
        if i==n or i==(n-1):
            print()
            print("Tiep tuc khong?",end="")
            x=str(input())
            if x=="K" or x=="k":
                break
            else:
                n=int(input("n="))
                inkq(n)
n=nhap()
i=inkq(n)