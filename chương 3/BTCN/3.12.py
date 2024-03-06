n=int(input())
r=''
if n>=0 and n<=9999:
    for i in str(n):
        if r==str(0):
            r=r+'A'
        elif i==str(1):
            r=r+'B'
        elif i==str(2):
            r=r+'C'
        elif i==str(3):
            r=r+'D'
        elif i==str(4):
            r=r+'E'
        elif i==str(5):
            r=r+'F'
        elif i==str(6):
            r=r+'G'
        elif i==str(7):
            r=r+'H'
        elif i==str(8):
            r=r+'K'
        elif i==str(9):
            r=r+'L'
    print(r)
else: print()