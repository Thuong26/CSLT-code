m=int(input(''))
while m>=0:
    t=1
    for j in range(1,m+1):
        t=t*j
    print(t)
    m=int(input(''))
    if m<0: break