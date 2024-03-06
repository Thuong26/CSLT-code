import math
def nhap():
    print('Nhap 3 so nguyen:')
    a=float(input('a='))
    while a==0:
        if a==0: a=float(input('a='))
    b=float(input('b='))
    while b==0:
        if b==0: b=float(input('b='))
    c=float(input('c='))
    while c==0:
        if c==0: c=float(input('c='))
    return a,b,c
def giaipt(a,b,c):
    x=b**2-4*a*c
    if x==0:
        return (-b/(2*a)),(-b/(2*a))
    elif x>0:
        return (-b+ math.sqrt(x))/(2*a),(-b-math.sqrt(x))/(2*a)
    else:
        return 'vo nghiem'
def inkq(x1,x2):
    if x1 != x2:
        print('Phuongtrinh co hai nghiem')
        print('x1=',x1,sep='')
        print('x2=',x2,sep='')
    elif x1== x2:
        print('Phuongtrinh co nghiem kep')
        print('x1=x2=',x1,sep='')
a,b,c=nhap()
if giaipt(a,b,c)!= 'vo nghiem':
    x1,x2=giaipt(a,b,c)
    inkq(x1,x2)
else: print('Phuongtrinh vo nghiem')