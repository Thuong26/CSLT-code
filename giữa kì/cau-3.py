import math


while True:
    n=int(input("n="))
    if 2<=n<=1000000:
        break
def kt(n):
    i=2
    while i<= math.sqrt(n):
        if n%2==0:
            return False
        i=i+1
    return True
while n>=2:
    if kt(n):
         print(n)
         break
    n=n-1
    