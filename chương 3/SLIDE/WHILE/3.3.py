i=1
while i<=9:
    j=1
    while j<=9:
        if len(str(i*j))==1:
            print(j*i,' '*2,end='')
        else:
            print(j*i,' ', end='')
        j=j+1
    i=i+1
    print(sep='')