n=input()
S=0
k=1
m=1
for i in n:
    if i==".":
        break
    k=k+1
for i in n:
    if m==k+1 or m==k+2 or m==k+3:
        S+=int(i)
    m+=1
print(S)
# 3/4
