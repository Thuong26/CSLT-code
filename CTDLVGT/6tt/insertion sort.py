a=[10,20,4,7,2,5]
for i in range(1,len(a)):
    x=a[i]
    pos=i
    while a[pos-1] > x and pos>0:
        a[pos]=a[pos-1]
        pos=pos-1
        print(a[pos])
    a[pos]=x
print(a)