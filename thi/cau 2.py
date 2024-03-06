a=int(input())
L=[]
while True:
    a=input()
    if a=='Q':
        t=0
        for i in L:
            if i%1==0:t=t+int(i)
        print(t)
        break
    L=L+float(a)
        