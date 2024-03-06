n=int(input('n='))
if n>=1:
    i=1
    while i<=n:
        if i%5==0:
            print(i)
        else:
            print(i,end=' ')
        i=i+1

