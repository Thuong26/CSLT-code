while True:
        n=int(input("n="))
        if 0<=n<=1000000:
            break
dem=0
for i in range(1,n+1):
    if i%2==0 and i%3==0:
        dem=dem+1
print(dem)