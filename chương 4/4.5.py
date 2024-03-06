from pickle import TRUE
from sys import flags
def lasont(x):
    if x<2: return False
    for i in range (2,x):
        if x%i==0: return True
def sohople(x):
    if x<=1: return True
    else: return False
def nhapvadem():
    print('Nhap day so:')
    x=int(input())
    dem=0
    while sohople(x)==False:
        if lasont(x):
            dem=dem+1
        x=int(input())
    return x,dem
def inkq(dem):
    print('Co',str(dem),'so nguyen to')
x,dem=nhapvadem()
inkq(dem)