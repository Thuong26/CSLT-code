for i in range(1,9):
    for j in range(1,9):
        if len(str(i*j))==1:
            print(j*i,' '*2,end='')
        else:
            print(j*i,' ', end='')
    print(sep='')