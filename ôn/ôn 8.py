s=input().split()
l=[]
for i in range(len(s)):
    if s[i] not in l:
        l.append(s[i])
for i in l:
    print(i,end=' ')

