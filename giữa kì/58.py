def nhap():
    n=int(input('n='))
    L=[]
    print(' moi nhap so nguyen')
    for i in range(0,n-1):
        x=int(input())
        L=L+[x]
    return L
def dem(L):
    dem=0
    for x in L: #duyet cac phan tu trong list
        if x%2==0:       
            dem=dem+1
    return dem
def inkq(dem):
    print('co',dem,'sochan')
L=nhap()
dem=dem(L)
inkq(dem)

    
