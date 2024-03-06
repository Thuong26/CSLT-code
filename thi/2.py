L=[]
n=input()
while True:
    if n =='Q':
        break
    L=L+[n]
    n=input()
S=0
for i in range(1,len(L),1):
    if float(L[i])<0:
        S+=abs(float(L[i]))
print(S)


        