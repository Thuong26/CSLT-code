t=int(input('n='))
if t>=1:
    l=1
    while l<=t:
        if l%5==0:
            print(l)
        else:
            print(l,end=' ')
        l=l+1

