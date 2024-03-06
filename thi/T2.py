def trungbinhconguoc(n):
    s=0
    t=0
    for i in range(1,n+1):
        if n%i==0:
            s=s+i
            t=t+1
    tbc=round(s/t,2)
    return tbc
while True:
    N=int(input())
    if N>0:
        print(trungbinhconguoc(N))
        break