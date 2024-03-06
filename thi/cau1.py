n=int(input())
L=[]
s=''
t=d=0
for i in range(n):
    a=input()
    s=s+a
for i in range(len(s)):
    if (s[i].isnumeric()==True) and i>=1:
        t=t+int(s[i])
        d=d+1
print(round((t/d),2))

