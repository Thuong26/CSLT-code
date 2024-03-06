def nhap():
    n=int(input('n='))
    return n
def inkq(n):
    while n>=2:
        for i in range(2,n+1,2):
            print(i,end=' ')
        m=str(input('\nTiep tuc khong?'))
        if m=='k' or m=='K':
            break 
        else: 
            n=int(input('n='))
            continue; 
n=nhap()
inkq(n)