a=int(input())
b=int(input())
while a>0 and b>0:
    s=0
    i=a
    if a>b: 
        a=int(input())
        b=int(input())
    else:
        while i<b:
            s+=i
            i+=1
        print (s)
        break
