s=input()
m=int(input())
if 1<=m<=20:
    j=1
    while j<=m:
        print((j-1)*(s+' ')+s)
        j=j+1
else: print()