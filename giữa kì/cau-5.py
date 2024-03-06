n=int(input())
s=0
for i in range(1,n+1):
    r=str(input())
if n<=100:
    for i in range(1,n+1):
        if r=='one':
            s=s+1
        elif r=='two':
            s=s+2
        elif r=='three':
            s=s+3
        elif r=='four':
            s=s+4
        elif r=='five':
            s=s+5
        elif r=='six':
            s=s+6
        elif r=='seven':
            s=s+7
        elif r=='eight':
            s=s+8
        elif r=='nine':
            s=s+9
print(s)