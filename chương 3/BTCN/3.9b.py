n=int(input(''))
if 2<=n<=50:
  m=1
  for m in range (1,n+1):
      if m%2==0:
          print(m,end=' ')