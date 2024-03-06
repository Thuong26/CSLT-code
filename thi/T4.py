T=[]
while True:
    n=input()
    if n=="T":
        s=0
        for i in T:
            if i%1!=0: s=s+i
        print(s)
        break
    T=T+[float(n)]