def nhap():
    n=int(input('n='))
    return n
def giaithua(n):
    gt=1
    if (n==0 or n==1):
        return gt
    else:
        for i in range (2,n+1):
            gt=gt*i
        return gt
def inkq(n,gt):
    print(str(n)+'!='+str(gt))
n=nhap()
gt=giaithua(n)
inkq(n,gt)