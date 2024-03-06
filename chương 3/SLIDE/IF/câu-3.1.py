a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
max=a
min=a
if b> max:
    max=b
if c> max: 
    max=c
print('SLN='+str(max))
if min>b:
    min=b
if min>c:
    min=c
print('SBN='+str(min))
