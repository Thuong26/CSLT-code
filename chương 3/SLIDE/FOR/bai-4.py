a=float(input('a='))
b=float(input('b='))
tt=input('Toan tu:')
while True:
    if tt=='+':
        print(str(a)+'+'+str(b)+'='+str(a+b))
    if tt=='-':
        print(str(a)+'-'+str(b)+'='+str(a-b))
    if tt=='*':
        print(str(a)+'*'+str(b)+'='+str(a*b))
    if tt=='/':
        print(str(a)+'/'+str(b)+'='+str(a/b))
    t=input('Tiep tuc:')
    print('a=',a)
    print('b=',b)
    tt=input('Toan tu:')
    if t=='T' or t=='t': break
    