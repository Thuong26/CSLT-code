a=float(input('x='))
b=float(input('y='))
pt=input('Phep toan:')
if pt=='+':
    print(str(a)+'+'+str(b)+'='+str(a+b))
if pt=='-':
    print(str(a)+'-'+str(b)+'='+str(a-b))
if pt=='*':
    print(str(a)+'*'+str(b)+'='+str(a*b))
if pt=='/':
    if b==0:
        print('Khong hop le')
    else: print(str(a)+'/'+str(b)+'='+str(a/b))
if pt!='+' and pt!='-' and pt!='*' and pt!='/':
    print('Khong hop le')