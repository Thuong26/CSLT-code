s=input()
l=[]
i=1
while i<len(s):
    if s[i].isdecimal() and (1<=int(s[i])<=9) and (i%2!=0):
        l.append(int(s[i]))  
    i=i+1
for i in l:
    print(i,end='')
