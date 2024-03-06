S=input()
s=1
t=0
for i in S:
    if i.isnumeric():
        s=s*int(i)
        t=1
if t==1: print(s)